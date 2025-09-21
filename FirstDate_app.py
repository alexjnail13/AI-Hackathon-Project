from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
llm = genai.GenerativeModel("gemini-2.5-pro")

def gemini_agent(user_input):
    response = llm.generate_content(user_input)
    return response.text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    step = request.form.get("step", "fashion")
    user_input = request.form.get("user_input", "")

    if request.method == "POST":
        if step == "fashion":
            if user_input.lower() == "y":
                response = llm.generate_content("What should I wear on a first date?").text
                step = "done"
            elif user_input.lower() == "n":
                step = "conversation"
        elif step == "conversation":
            if user_input.lower() == "y":
                response = llm.generate_content("What are some good conversation topics for a first date?").text
                step = "done"
            elif user_input.lower() == "n":
                step = "ideas"
        elif step == "ideas":
            if user_input.lower() == "y":
                response = llm.generate_content("What are some good first date ideas?").text
                step = "done"
            elif user_input.lower() == "n":
                response = "Alright, if you need anything else, just ask!"
                step = "done"
        elif step == "done":
            if user_input:
                response = gemini_agent(user_input)
    else:
        step = "fashion"

    return render_template("index.html", response=response, step=step)

if __name__ == "__main__":
    app.run(debug=True)