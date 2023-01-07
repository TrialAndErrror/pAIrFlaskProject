from .. import db
import datetime


# Define a model for the commands
class VolumeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calorie_density = db.Column(db.Integer, nullable=False)
    final_volume = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<VolumeRequest ({self.final_volume} @ {self.calorie_density} cal)>' % self.command
