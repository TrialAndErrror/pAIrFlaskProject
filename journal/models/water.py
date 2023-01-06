import datetime
from flask import jsonify

from .. import db


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


def make_water(amount):
    new_entry = Water(amount=amount)

    db.session.add(new_entry)
    db.session.commit()

    return f'Water entry recorded: {amount}.'


def get_waters(date):
    if date:
        return jsonify(Water.query.filter(Water.created_at == date).all())
    else:
        return jsonify(Water.query.all())