from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# {"verb": "eat", "noun": "mango"}

@app.get('/homepage')
def make_form():
    # Render the madlib home page form

    return render_template("questions.html", prompts=silly_story.prompts)

# TODO: docstrings in python have 3 double quotes and can span multiple lines
# snake case for naming


@app.get('/results')
def show_story():
    # Render a story created from inputs from the home page

    buildStory = silly_story.get_result_text(request.args)
    return render_template("results.html", results=buildStory)
