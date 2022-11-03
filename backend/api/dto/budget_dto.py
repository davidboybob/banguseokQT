from flask_restx import Namespace, fields

class BudgetDto:
    api = Namespace(name='budget', description="budget 관련 API")
    budget = api.model(
        'budget',
        {
            # 'id': fields.Integer(readonly=True, description="budget 고유 id"),
            'mount': fields.Integer(description="budget 예산 정보"),
            # 'donation_id': fields.List(fields.Integer, description="budget donation id"),
            # 'challenges_id': fields.List(fields.Integer, description="budget challenges 이전비")
        }
    )
