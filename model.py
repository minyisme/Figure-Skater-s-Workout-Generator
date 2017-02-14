"""Models and database functions for project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#######################
#DB class#
#######################

# #ISI Levels
# class ISI(db.Model):
#     """ISI Levels"""
    
#     __tablename__ = "isi"

#     level = db.Column(db.String(20), nullable=False, primary_key=True)

#     def __repr__(self):
#         """Provides helpful representation when printed"""

#         return ("<ISI level=%s>" % (self.level))

# #USFS Levels
# class USFS(db.Model):
#     """USFS Levels"""
    
#     __tablename__ = "usfs"

#     level = db.Column(db.String(20), nullable=False, primary_key=True)

#     def __repr__(self):
#         """Provide helpful representation when printed"""

#         return ("<USFS level=%s>" % (self.level))

#Skating exercises
class Exercise(db.Model):
    """Skating Exercises"""

    __tablename__ = "exercises"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(20))
    #categorizes under isi level
    isi_level = db.Column(db.String(20), nullable=False)
    #categorizes under usfs level
    usfs_level = db.Column(db.String(20))

    # #define relationship to isi levels
    # isi = db.relationship('ISI', backref='exercises')
    # #define relationship to usfs levels
    # usfs = db.relationship('USFS', backref='exercises')

    def __repr__(self):
        """Provide helpful representation when printed"""

        return("<Exercise id=%s name=%s type=%s isi_level=%s usfs_level=%s>" % (self.id, self.name, self.type, self.isi_level, self.usfs_level))

######################
#Helper functions
######################

def connect_to_db(app):
    """Connect the database to app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///skatedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # Allows interaction directly with db from
    # server when running interactively

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."



