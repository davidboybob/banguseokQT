from models.models import db
from models.models import Budget

def get_all_budget():
    return Budget.query.all()