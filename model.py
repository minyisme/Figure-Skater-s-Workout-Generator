"""Models and database functions for project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#######################
#DB class#
#######################

#ISI Levels
class ISI(db.Model):
    """ISI Levels"""
    
    __tablename__ = "isi"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    level = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """Provides helpful representation when printed"""

        return ("<ISI id=%s level=%s>" % (self.id, self.level))

#USFS Levels
class USFS(db.Model):
    """USFS Levels"""
    
    __tablename__ = "usfs"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    level = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return ("<USFS id=%s level=%s>" % (self.id, self.level))

#Skating exercises
class Exercise(db.Model):
    """Skating Exercises"""

    __tablename__ = "exercises"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.string(200), nullable=False)
    type = db.Column(db.string(20))
    #categorizes under isi level
    isi_id = db.Column(db.Integer, db.ForeignKey('isi.id'), nullable=False)
    #categorizes under usfs level
    usfs_id = db.Column(db.Integer, db.ForeignKey('usfs.id'), nullable=False)

    #define relationship to isi levels
    isi_level = db.relationship('ISI', backref='exercises')
    #define relationship to usfs levels
    usfs_level = db.relationship('USFS', backref='exercises')

    def __repr__(self):
        """Provide helpful representation when printed"""

        return("<Exercise id=%s name=%s type=%s isi_id=%s usfs_id=%s>" % (self.id, self.name, self.type, self.isi_id, self.usfs_id))

######################
#Helper functions
######################

def connect_to_db(app):
    """Connect the database to app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///travels'
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



