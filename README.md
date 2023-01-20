# ABASTILLAS_ELGARAN_ESPINO_PARCON_UNATING THESIS
## Synopsis

Text can often be difficult to read and understand especially for people with functional illiteracy, cognitive impairment, or poor language skills. Easi is a study in text simplification using natural language processing which aims to help students from grades 4-6 by simplifying text to make it easier for them to comprehend the lessons of the subject matter, specifically English.

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Backend Setup
The original backend for the application has already been deployed to [Render](https://easi-backend.onrender.com) with /translate as the endpoint for putting responses, however if you wish to run it on your local computer here are the steps to do so. 

1. Create a virtual environment by typing out `python -m venv $ENV_NAME`
2. Activate virtual environment `.\venv\Scripts\activate `
3. Create an `.env` file and name it `OPENAI_KEY` ex. `OPENAI_KEY.env`
4. Inside of the .env file paste `OPENAI_KEY=sk-L9zG---` the value of OPENAI_KEY should be your API key from OpenAI GPT-3
5. Run `pip install -r requirements.txt` on your terminal

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)
