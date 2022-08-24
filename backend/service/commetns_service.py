from models.models import db
from models.models import Comments

def get_all_comments():
    return Comments.query.all()