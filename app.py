from flask import Flask, jsonify, render_template, request, redirect, url_for
from scribe import *
from multiprocessing import Queue
import openai
import shelve

app = Flask(__name__)
STORE = shelve.open("datastore")

PROMPT_HEADER = f"""
        Summarize the following transcript. Write using the following format. Replace everything in <> brackets.

        Main Points:
        - <main point 1> : by <speaker 1>
        - <main point 2> : by <speaker 2>
        - <and so on> : by <and so on>

        Action Items:
        - <action 1> : by <speaker 1>
        - <action 2> : by <speaker 2>
        - <and so on> : by <and so on>

        Highights: 
        - <highlight 1>
        - <highlight 2>
        - <and so on>

        Recent Summary: 
        <short summary of the transcript>

        Transcript:

        """


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prompt")
def prompt():
    return render_template("prompt.html")

@app.route("/meeting", methods=["POST"])
def post_user_prompt():
    request_data = request.get_json()
    print(request_data)
    try:
        request_time=request_data["date"]
        transcript_id = get_most_recent_transcript_id(STORE["google_creds"], folder_id=STORE["folder_id"], datetime=request_data["meeting"])
        print("##############")
        print(transcript_id)
        STORE["transcript_id"] = transcript_id
        print("##############")
    except HttpError as err:
        print(err)
    return jsonify(dict(response="200"))

@app.route("/summary", methods=["GET"])
def summary():
    doc_service = build('docs', 'v1', credentials=STORE["google_creds"])
    action_items = []
    main_points = []
    highlights = []
    print("^^^^^^^^^^^^^^^^^^^^^^^^")
    transcript_id = STORE["transcript_id"]
    print(STORE["transcript_id"])
    document = doc_service.documents().get(documentId=transcript_id['id']).execute()
    doc_content = document.get('body').get('content')
    transcript = read_structural_elements(doc_content)
    prompt = PROMPT_HEADER + transcript
    # GENERATOR.generate(prompt=prompt,
    #                engine='davinci',
    #                max_tokens=20,
    #                temperature=0.5,
    #                top_p=1)
    completion = openai.Completion.create(engine="davinci", prompt=prompt)
    print(completion.choices[0].text)
    resp_groups = split(completion.choices[0].text, ['Main Points:', 'Action Items:', 'Highights:', 'Recent Summary:'])
    
    for point in resp_groups[1].split('\n'):
        if point not in main_points:
            main_points.append(point)
    
    for action in resp_groups[2].split('\n'):
        if action not in action_items:
            action_items.append(action)
    
    for action in resp_groups[3].split('\n'):
        if action not in action_items:
            highlights.append(action)

    summary = resp_groups[3]

    return jsonify(dict(mainpoints=main_points, 
                        action_items=action_items,
                        highlights=highlights,
                        summary=summary))


if __name__ == "__main__":
    creds = get_credentials(force=False)
    STORE["google_creds"] = creds
    # CHAT = get_gpt_chat(email="srinivas.thestallion.vishal@gmail.com", password="$Birth$1995$")
    openai.api_key = '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'
    # set_api_key(KEY)
    # GENERATOR = GPT3Generator(input_text="Template for Meeting summarization with meeting transcript", output_text="Filled Template")
    folderid = get_folder(creds)
    STORE["folder_id"] = folderid
    app.run(host="0.0.0.0", port=8080)