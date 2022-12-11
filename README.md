# scribe ai

Here's [our product video](https://devpost.com/software/scribe-qvte7g)!

Zoom in on productivity with automated meetings! Scribe is an automated note-taking application that enables users to focus on the call or quickly catch up on anything they missed.

## How it works

The scribe pipeline can be broken into the following sections:
1. Generate real-time meeting transcription as google drive doc
2. Extract transcript from google drive using oauth
3. Get user input to generate prompt
4. Call GPT to get summary
5. Combine summary into running summary for real-time presentation
6. Display information to user!

## Installation

There are a few manual steps before being able to run scribe.

### Install Meet Transcript

This is a google chrome plugin that reads captions and saves them in Google Drive.

[Download here](https://chrome.google.com/webstore/detail/meet-transcript/jkdogkallbmmdhpdjdpmoejkehfeefnb?hl=en)!

### Get oauth Token

Email Jef (jef@sendit.ai), or reach Jef on Discord (Jef 🧶🐊 #7404). You'll need both of the following to oauth gdrive:
* app_credential.json file put in this (.../scribe) directory.
* added as a "test user" on google cloud.

### Install Required Libraries 

Run the following command
```
pip install -r requirements.txt
```

## Running

The workflow is the following:
1. Start meeting
2. go to your google drive to get document handle
3. start scribe
4. input document handle into scribe
5. start summarization!

### Running scribe

In web mode:
```
python3 app.py
```

In terminal mode:
You MUST enter your OpenAI login details in `scribe.py` in the function: `get_gpt_chat(email="", password="")`. Then run:
```
python3 scribe.py
```

IMPORTANT: During oauth, you must press 'continue' on the left!

## Contributors

[Jef Packer](https://github.com/jbpacker)
[Srinivas Venkatanarayanan](https://github.com/Vi-Sri)