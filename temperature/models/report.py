import datetime

from temperature import db


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(), nullable=False)
    humidity = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return '<Command %r>' % self.command

    def serialize(self):
        return {
            "id": self.id,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "created_at": self.created_at
        }


def make_report(temperature, humidity):
    new_entry = Report(temperature=temperature, humidity=humidity)

    db.session.add(new_entry)
    db.session.commit()

    return dict(
        message=f'Temperature report entry recorded: {temperature} degrees & {humidity} % humidity.',
        success=True
    )


def get_reports(date):
    if date:
        return Report.query.filter(Report.created_at == date).all()
    else:
        return Report.query.all()
