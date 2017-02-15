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

    # gets input from user
    level = str(request.args.get("skater-level"))
    time = str(request.args.get("practice-time"))
    exercise_types = request.args.getlist("exercise-type")

    # change unicode to string
    exercise_types_str = []
    for exercise in exercise_types:
        exercise_types_str.append(str(exercise))

    # gets all relevant exercises to user's level
    rel_levels = functions.relevant_levels(level)
    all_exercises = functions.all_exercises(rel_levels)

    # print "rel levels", rel_levels

    # gets all types of exercises user wants to practice
    db_ex_types = []
    for a_type in exercise_types_str:
        print "yoyoyoy", a_type
        print type(a_type)
        db_ex_types.append(functions.type_to_dbtype(a_type))

    # print db_ex_types

    # gets number of exercises of each type to practice
    num_ex = functions.num_exercises(time, db_ex_types)

    # print num_ex

    # gets all exercises of a relevant type
    rel_ex = functions.exercises_by_type(all_exercises, db_ex_types)

    # print rel_ex

    # for each exercise type in db_ex_types, gets num_ex of random exercises
    practice = []
    for each in rel_ex:
        practice.append(functions.rand_exercises(each, num_ex))

    # print "PRACTICE!!!!!!", practice

    return render_template("homepage.html")













if __name__ == "__main__":
#     # We have to set debug=True here, since it has to be True at the point
#     # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

#     # Use the DebugToolbar
#     DebugToolbarExtension(app)

    app.run()