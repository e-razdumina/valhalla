from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.valhalla

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        name = request.form['name']
        story = request.form['story']
        source = request.form['degree']
        todos.insert_one({'char_name': name, 'char_desc': story, 'source': source})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)
