from bdb import BdbQuit
from flask import request
from flask_restx import Api, Resource, Namespace

from service.budget_service import get_all_budget
from utils.dto import BudgetDto

api = BudgetDto.api
_budget = BudgetDto.budget

@api.route('/')
class BudgetList(Resource):
    @api.doc('list_of_Donation')
    @api.marshal_list_with(_budget, envelope='data')
    def get(self):
        return get_all_budget()
