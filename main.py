from re import template
from flask import Flask, render_template, request, redirect
from models import db, PostModel

# initialize and setup app
app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/Employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# create table
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']
        post = PostModel(title, content, date)
        db.session.add(post)
        db.session.commit()
        return render_template('index.html')
