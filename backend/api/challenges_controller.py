from flask import request
from flask_restx import Api, Resource, Namespace

from service.challenges_service import get_all_challenges
from utils.dto import ChallengesDto

api = ChallengesDto.api
_challenges = ChallengesDto.challenges

@api.route('/')
class ChallengesList(Resource):
    @api.doc('list_of_Challenges')
    @api.marshal_list_with(_challenges, envelope='data')
    def get(self):
        return get_all_challenges()
