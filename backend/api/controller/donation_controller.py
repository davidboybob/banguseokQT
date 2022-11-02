from flask import request
from flask_restx import Api, Resource, Namespace

from api.service.donation_service import get_all_donation
from utils.dto import DonationDto

api = DonationDto.api
_donation = DonationDto.donation

@api.route('/')
class DonationList(Resource):
    @api.doc('list_of_Challenges')
    @api.marshal_list_with(_donation, envelope='data')
    def get(self):
        return get_all_donation()
