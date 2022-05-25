from marshmallow import Schema, fields
from setup_db import db


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())


class GenreSchema(Schema):
    name = fields.Str()


genre_schema = GenreSchema()
