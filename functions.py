"""Functions for project"""

from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, Exercise
import random


def relevant_levels(level):
    """Gets all relevant levels based on user input"""

    # list all levels
    levels = ["Pre-Alpha", "Alpha", "Beta", "Gamma", "Delta", "Freestyle 1", "Freestyle 2", "Freestyle 3", "Freestyle 4", "Freestyle 5", "Freestyle 6", "Freestyle 7", "Freestyle 8", "Freestyle 9", "Freestyle 10"]

    # add all relevant levels to a list
    relevant_levels = []
    for each in levels:
        if each != level:
            relevant_levels.append(each)
        else:
            relevant_levels.append(each)
            break

    return relevant_levels

def all_exercises(relevant_levels):
    """Gets all exercises from database based on the relevant levels"""

    exercises = []
    # for each level relevant to user, get all exercises for that level from db
    for level in relevant_levels:
        exercises_by_level = (Exercise.query.filter_by(isi_level=level).all())
        # add each exercise from resulting list from db to exercises
        for exercise in exercises_by_level:
            exercises.append(exercise)

    return exercises

def type_to_dbtype(type):
    """Gets a db type from types in the input field"""

    if type == "Jumps":
        return ["Jump"]
    elif type == "Spins":
        return ["Spin"]
    elif type == "Edges":
        return ["Edge"]
    elif type == "Footwork":
        return ["Turn", "Stop"]


def exercises_by_type(exercises, types):
    """Filters all exercises by type"""

    # add all exercises of a type to list
    exercises_of_type = []
    for exercise in exercises:
        for type in types:
        if exercise.type==type:
            exercises_of_type.append(exercise.name)

    return exercises_of_type










