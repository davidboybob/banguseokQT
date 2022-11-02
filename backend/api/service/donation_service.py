from models.models import db
from models.models import Donation

def get_all_donation():
    return Donation.query.all()