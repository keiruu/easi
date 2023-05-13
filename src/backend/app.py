from flask import Flask
from flask import Flask, render_template, request
from datetime import date
from flask_cors import CORS, cross_origin
import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv('.env')

#OPENAI GPT-3 API KEY
openai.api_key = os.environ.get('OPENAI_KEY')

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def index():
    return "GPT-3 Playground"

#https://easi-backend.herokuapp.com/translate
#ENDPOINT FOR GETTING THE SIMPLIFIED TEXT
#FORMAT OF REQUEST: 
#{ prompt: TEXT TO BE SIMPLIFIED }
@app.route("/translate", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def translate():
    if request.method == "POST":
        # intro = "A second grader asked me what this passage means:\n\"\"\"\n"
        # outro = "\n\"\"\"\nI rephrased it for him, in plain language a second grader can understand:\n\"\"\"\n"
        intro = "Summarize in plain language a second grader can understand: \n"
        prompt = request.json["prompt"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt= intro + prompt ,
            # temperature=0,
            # max_tokens=100,
            # top_p=1.0,
            # frequency_penalty=0.0,
            # presence_penalty=0.0,
            stop=["\"\"\""],
            # model="text-davinci-002",
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = response.choices[0].text
        print(text)
        list = text.split('\n')[1:]
        list = filter(None, list)
        offset = 0
        return response["choices"][0]["text"].strip()
    else:
        return ""


# HEROKU NOTES
# update app:
# commit then type 'git push heroku main'

# ACTIVATE VIRTUAL ENVIRONMENT
# .\venv\Scripts\activate 

# How did the Render setup work just incase I forget
# Added dotenv and .env file to place key
# activated virtual environment
# typed 'set OPENAI_KEY=""' on the terminal
# from there I just had to set up environment variables on render and I guess i'm good to go

# prompt format:
# {
# 	"prompt": "text"
# }
#