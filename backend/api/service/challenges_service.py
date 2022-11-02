from urllib import response
from models.models import db
from models.models import Challenges

def get_all_challenges():
    return Challenges.query.all()