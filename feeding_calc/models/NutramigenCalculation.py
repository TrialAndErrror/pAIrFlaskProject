from .. import db
import datetime
from decimal import Context


class NutramigenCalculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calorie_density = db.Column(db.Float)
    total_volume = db.Column(db.Float)
    nutramigen_scoops = db.Column(db.Numeric(100, 4))
    nutramigen_grams = db.Column(db.Numeric(100, 4))

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, calorie_density, total_volume):
        super().__init__()
        self.calorie_density = calorie_density
        self.total_volume = total_volume

        # Calculate the amount of Nutramigen needed based on the calorie density and total volume
        scoops, grams = calculate_scoops(
            volume=total_volume,
            calorie_density=calorie_density
        )

        self.nutramigen_scoops = scoops
        self.nutramigen_grams = grams


def calculate_scoops(volume, calorie_density):
    ratio = Context(prec=4).create_decimal(calorie_density) / Context(prec=4).create_decimal('20')

    # Adjust volume to compensate for added volume of powder in formula
    adjusted_volume = Context(prec=10).create_decimal(volume) * (Context(prec=10).create_decimal('.9') * ratio)

    scoops_to_water = ratio / Context(prec=10).create_decimal('60')

    scoops = scoops_to_water * adjusted_volume

    grams = Context(prec=10).create_decimal('9') * scoops

    return scoops, grams

