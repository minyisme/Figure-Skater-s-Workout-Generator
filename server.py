"""Server for project"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
# add tables from model.py when ready
from model import connect_to_db, db, Exercise
import functions

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# raises error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage + workout generator."""

    return render_template("homepage.html")



@app.route('/generate', methods=["GET"])
def generate():
    """Workout result"""

    level = request.args.get("skater-level")
    time = request.args.get("practice-time")
    exercise_types = request.args.getlist("exercise-type")

    print level, time, exercise_types

    return render_template("homepage.html")













if __name__ == "__main__":
#     # We have to set debug=True here, since it has to be True at the point
#     # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

#     # Use the DebugToolbar
#     DebugToolbarExtension(app)

    app.run()