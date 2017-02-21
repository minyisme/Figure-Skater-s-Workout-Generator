<dl id="fare-share"></dl>
# Figure Skater Workout Generator

Figure Skater Workout Generator is an app built for figure skaters who want a set of skating exercises to work on during their time on the ice. It allows a user to easily enter their skating level, the amount of time they want to spend on the ice, and the type of exercises they want to do. Based on the information entered, the app will then generate a series of elements for the skater to practice. 


## Tech Stack                   

[Python](https://www.python.org/), [Flask](http://flask.pocoo.org/), [SQLAlchemy](http://www.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/), [Jinja2](http://jinja.pocoo.org/docs/dev/), HTML, CSS


## Features

##### Landing Page

![alt text](https://github.com/minyisme/Figure-Skater-s-Workout-Generator/blob/master/static/images/landing_page.png)

- User enters their workout parameters
![alt text](https://github.com/minyisme/Figure-Skater-s-Workout-Generator/blob/master/static/images/user_preferences.png)

##### Workout Results Page

![alt text](https://github.com/minyisme/Figure-Skater-s-Workout-Generator/blob/master/static/images/workout.png)


## Get the Figure Skater's Workout Generator

Clone or fork this repo:

```
https://github.com/minyisme/Figure-Skater-s-Workout-Generator
```

Create and activate a virtual environment inside your project directory:

```
virtualenv env
source env/bin/activate
```

Install the requirements:

```
pip install -r requirements.txt
```

Set up your database and seed exercises data:

```
python model.py
python seed.py
```

Start running your server:

```
python server.py
```

Navigate to 'localhost:5000/' and have fun with your workout!


## For Version 2.0

- **One page app:** A one page mobile friendly interface.
- **Deployment:** Deployment using Heroku
- **User preferences:** Allow for user log in for personal preferences