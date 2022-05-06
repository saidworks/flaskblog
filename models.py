import datetime
from flask_sqlalchemy import SQLAlchemy

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

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.Text(), nullable=True)
    date = db.Column(MyDateTime, nullable=True)

    def __init__(self, title, content, date):
        count = 1
        self.post_id = count
        self.title = title
        self.content = content
        self.date = date
        count += 1

    def __repr__(self):
        return f"{self.title}: {self.content} written by Said Zitouni on {self.date}"
