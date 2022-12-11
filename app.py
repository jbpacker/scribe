from flask import Flask, jsonify, render_template, request
from scribe import *
from multiprocessing import Queue

app = Flask(__name__)

CREDS = None
CHAT = None 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meeting", methods=["POST"])
def post_user_prompt():
    request_data = request.get_json()
    print(request_data)
    try:
            transcript_id = get_most_recent_transcript_id(CREDS)
            doc_service = build('docs', 'v1', credentials=CREDS)
    except HttpError as err:
            print(err)

    return jsonify(dict(response=request_data))

@app.route("/prompt", methods=["GET"])
def get_user_prompt():
    return jsonify(dict(response="get"))


if __name__ == "__main__":
    CREDS = get_credentials(force=False)
    CHAT = get_gpt_chat(email="srinivas.thestallion.vishal@gmail.com", password="$Birth$1995$")
    
    app.run(host="0.0.0.0", port=8080, debug=True)