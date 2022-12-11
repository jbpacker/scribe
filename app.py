from flask import Flask, jsonify, render_template, request
from scribe import *
from multiprocessing import Queue

app = Flask(__name__)

CREDS = None
CHAT = None
FOLDERID = None
TRANSCRIPT_ID = None
REQUEST_DATETIME = None

PROMPT_HEADER = f"""
        Summarize the following transcript. Write using the following format. Replace everything in <> brackets.

        Main Points:
        - <main point 1> : <speaker 1>
        - <main point 2> : <speaker 2>
        - <and so on> : <and so on>

        Action Items:
        - <action 1> : <speaker 1>
        - <action 2> : <speaker 2>
        - <and so on> : <and so on>

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

@app.route("/meeting", methods=["POST"])
def post_user_prompt():
    request_data = request.get_json()
    print(request_data)
    try:
        REQUEST_DATETIME=request_data["date"]
        TRANSCRIPT_ID = get_most_recent_transcript_id(CREDS, folder_id=FOLDERID, datetime=request_data["meeting"])
        print("##############")
        print(TRANSCRIPT_ID)
        print("##############")
    except HttpError as err:
        print(err)
    return render_template("prompt.html")

@app.route("/summary", methods=["GET"])
def get_user_prompt():
    doc_service = build('docs', 'v1', credentials=CREDS)
    action_items = []
    main_points = []
    highlights = []
    document = doc_service.documents().get(documentId=TRANSCRIPT_ID).execute()
    doc_content = document.get('body').get('content')
    transcript = read_structural_elements(doc_content)
    prompt = PROMPT_HEADER + transcript
    answer = CHAT.ask(prompt)
    resp_groups = split(answer[0], ['Main Points:', 'Action Items:', 'Highights:', 'Recent Summary:'])
    
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
    CREDS = get_credentials(force=False)
    # CHAT = get_gpt_chat(email="srinivas.thestallion.vishal@gmail.com", password="$Birth$1995$")
    FOLDERID = get_folder(CREDS)
    app.run(host="0.0.0.0", port=8080, debug=True)