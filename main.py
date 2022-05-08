from re import template
from flask import Flask, render_template, request, redirect
from models import db, PostModel

# initialize and setup app
app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/Blog.db'
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
        author = request.form['author']
        post = PostModel(title, content, date, author)
        db.session.add(post)
        db.session.commit()
        return redirect('/')


@app.route('/')
def index():
    if request.method == "GET":
        posts = PostModel.query.all()
        return render_template("index.html", posts=posts)


@app.route('/<int:id>')
def retreivePost(id):
    post = PostModel.query.filter_by(post_id=id).first()
    if post:
        return render_template('post.html', post=post)
    return f"Post with id{id} does not exist"


@app.route('/<int:id>/update', methods=["GET", "POST"])
def updatePost(id):
    post = PostModel.query.filter_by(post_id=id).first()
    print(post)
    if request.method == "POST":
        if post:
            db.session.delete(post)
            db.session.commit()
            title = request.form['title']
            content = request.form['content']
            date = request.form['date']
            author = request.form['author']
            post = PostModel(id, title, content, date, author)
            db.session.add(post)
            db.session.commit()
            redirect(f"/{id}")
        else:
            return f"Post with id ={id} does not exist"
    return render_template('post.html', post=post)


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    post = PostModel.query.filter_by(post_id=id).first()
    if request.method == 'POST':
        if post:
            db.session.delete(post)
            db.session.commit()
            return redirect('/')
        else:
            return redirect('/')
    return render_template('delete.html', post=post)
