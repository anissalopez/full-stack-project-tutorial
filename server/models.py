from sqlalchemy_serializer import SerializerMixin
from config import db


class Movie(db.Model, SerializerMixin):
    __tablename__ ='movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    def __repr__(self):
        return f'Movie: {self.title}'