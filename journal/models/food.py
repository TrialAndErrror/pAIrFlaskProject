import datetime

from flask import jsonify
from .. import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


def make_food(amount, name):
    new_entry = Food(amount=amount, name=name)

    db.session.add(new_entry)
    db.session.commit()

    return f'Food entry recorded: {amount} of {name}.'


def get_foods(date):
    if date:
        return jsonify(Food.query.filter(Food.created_at == date).all())
    else:
        return jsonify(Food.query.all())
