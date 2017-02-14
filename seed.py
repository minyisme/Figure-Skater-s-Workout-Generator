"""Utility file to seed skate db from seed files"""

from sqlalchemy import func
from model import Exercise

from model import connect_to_db, db
from server import app

import csv

def load_isi():
    """Load ISI levels from ISI.csv into database"""

    print "ISI"

    # Delete all rows in table, so if we need to
    # run this a second time, we won't be trying
    # to add duplicate levels.
    ISI.query.delete()

    # Read isi.csv file and insert data
    counter = 0
    dictISI = {}

    with open('seed_files/ISI.csv', 'rb') as all_isi:
        isi_info = csv.reader(all_isi)
        for row in isi_info:
            level = row[0]
            counter += 1

            isi = ISI(level=level)

            db.session.add(isi)

    db.session.commit()

    print "Loaded"

def load_usfs():
    """Load USFS levels from ISI.csv into database"""

    print "USFS"

    # Delete all rows in table, so if we need to
    # run this a second time, we won't be trying
    # to add duplicate levels.
    USFS.query.delete()

    # Read usfs.csv file and insert data
    counter = 0
    dictUSFS = {}

    with open('seed_files/USFS.csv', 'rb') as all_usfs:
        usfs_info = csv.reader(all_usfs)
        for row in usfs_info:
            level = row[0]
            counter += 1

            usfs = USFS(level=level)

            db.session.add(usfs)

    db.session.commit()

    print "Loaded"

def load_exercises():
    """Load skating exercises from Exercises.csv into database"""

    print "Exercises"

    # Delete all rows in table, so if we need to
    # run this a second time, we won't be trying
    # to add duplicate exercises.
    Exercise.query.delete()

    # Read exercises.csv file and insert data
    counter = 0
    dictexercises = {}

    with open('seed_files/Exercises.csv', 'rb') as all_exercises:
        exercises_info = csv.reader(all_exercises)
        for row in exercises_info:
            name, type, isi_level, usfs_level = row[0], row[1], row[2], row[3]
            counter += 1

            exercise = Exercise(name=name, type=type, isi_level=isi_level, usfs_level=usfs_level)

            db.session.add(exercise)

    db.session.commit()

    print "Loaded"

if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    # load_isi()
    # load_usfs()
    load_exercises()