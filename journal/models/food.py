import datetime

from journal import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


def make_food(amount, name):
    if not amount:
        return dict(
            message=f'Missing Food Amount',
            success=False
        )

    if not name:
        return dict(
            message=f'Missing Food Name',
            success=False
        )
    new_entry = Food(amount=amount, name=name)

    db.session.add(new_entry)
    db.session.commit()

    return dict(
        message=f'Food entry recorded: {amount} of {name}.',
        success=True
    )


def get_foods(date):
    if date:
        return Food.query.filter(Food.created_at == date).all()
    else:
        data = Food.query.all()
        return data
