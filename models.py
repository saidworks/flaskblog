from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# define the post model


class PostModel(db.Model):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.Text(), nullable=True)
    date = db.Column(db.DateTime(), nullable=True)
    author = db.Column(db.String())

    def __init__(self, post_id, title, content, date, author):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.date = date
        self.author = author

    def __repr__(self):
        return f"{self.title}: {self.content} writter by {self.author} on {self.date}"
