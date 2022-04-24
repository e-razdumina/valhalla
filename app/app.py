from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.valhalla

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        story = request.form['story']
        source = request.form['degree']
        comment = request.form['comment']
        type = request.form['type']
        todos.insert_one({'char_name': name, 'char_desc': story, 'source': source, 'comment': comment, 'type': type})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


if __name__ == "__main__":
    print(("* Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)
