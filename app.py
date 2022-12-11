from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def post_user_prompt():
  return jsonify(dict(response="post"))

@app.route("/prompt", methods=["GET"])
def get_user_prompt():
    return jsonify(dict(response="get"))


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)