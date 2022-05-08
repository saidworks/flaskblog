import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()


# cast string to datetime
class MyDateTime(db.TypeDecorator):
    impl = db.DateTime

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            return datetime.datetime.strptime(value, '%Y-%m-%d')
        return value


# define the post model
class PostModel(db.Model):
    __tablename__ = "post"

    post_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.Text(), nullable=True)
    date = db.Column(MyDateTime, nullable=True)
    author = db.Column(db.String(), nullable=True)

    def __init__(self, *args):
        if len(args) == 4:
            self.title = args[0]
            self.content = args[1]
            self.date = args[2]
            self.author = args[3]
        elif len(args) == 5:
            self.post_id = args[0]
            self.title = args[1]
            self.content = args[2]
            self.date = args[3]
            self.author = args[4]

    def __repr__(self):
        return f"{self.title}: {self.content} written by {self.author} on {self.date}"
