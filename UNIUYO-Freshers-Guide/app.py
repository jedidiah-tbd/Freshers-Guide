from flask import Flask, render_template, request, jsonify
from ai_engine import get_ai_response

app = Flask(__name__)

# ==========================
# WEBSITE PAGES
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/fees")
def fees():
    return render_template("fees.html")


@app.route("/screening")
def screening():
    return render_template("screening.html")


@app.route("/four-files")
def four_files():
    return render_template("four-files.html")


@app.route("/course-reg")
def course_registration():
    return render_template("course-reg.html")


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")


@app.route("/ai")
def ai():
    return render_template("ai.html")


# ==========================
# AI CHAT API
# ==========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()

    if message == "":
        return jsonify({
            "reply": "Please type a question."
        })

    try:

        reply = get_ai_response(message)

    except Exception as e:

        print(e)

        reply = (
            "Sorry, something went wrong while processing your request."
        )

    return jsonify({
        "reply": reply
    })


# ==========================
# START SERVER
# ==========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )