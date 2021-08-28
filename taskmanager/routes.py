from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task, Day


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template('categories.html')


@app.route("/add_category", methods=("GET", "POST"))
def add_category():
    return render_template("add_category.html")


@app.route("/add_task")
def add_task():
    return render_template("add_task.html")
