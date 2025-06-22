from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Tadas"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beatufiul day in Portland!" 
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie is so cool!"
        },
        {
            "author": {"username": "Ryan"},
            "body": "Does anyone know a nice ramen place in Prague?"
        },
        {
            "author": {"username": "Tyler"},
            "body": "My dog just ran away..."
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)