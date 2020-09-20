from flask import Flask,render_template
from . import main

#views
@main.route('/')
def index():
    title = 'PitchApp- An application where 1 minute or 60 seconds can make you or break you'
    return render_template('index.html' ,title = title)

@main.route('/about')
def about():
    title = 'About PitchApp'
    return render_template('about.html')