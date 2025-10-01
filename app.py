import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'woc+*(,^c~L#j{;'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # get a connection to our db
    conn = get_db_connection()
    # gets each row
    posts = conn.execute('SELECT * FROM posts').fetchall()
    print(posts) # Prints posts to the server's terminal
    conn.close()
    return render_template('index.html', posts=posts)

# processes requests to create/ - both GET and POST request types
@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

app.run(debug=True, port=5500)