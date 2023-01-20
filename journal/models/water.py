import datetime
from journal import db


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


def make_water(amount):
    if not amount:
        return dict(
            message=f'Missing Water Amount',
            success=False
        )

    new_entry = Water(amount=amount)

    db.session.add(new_entry)
    db.session.commit()

    return dict(
        message=f'Water entry recorded: {amount}.',
        success=True
    )


def get_waters(date):
    if date:
        return Water.query.filter(Water.created_at == date).all()
    else:
        return Water.query.all()
