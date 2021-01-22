from app import db
from sqlalchemy.dialects.postgresql import JSON


class Card(db.Model):
    __tablename__ = 'Cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    attributes = db.Column(JSON)

    def __init__(self, name, description, attributes):
        self.name = name
        self.description = description
        self.attributes = attributes

    def __repr__(self):
        return '<id {}>'.format(self.id)
