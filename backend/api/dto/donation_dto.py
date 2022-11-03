from flask_restx import Namespace, fields


class DonationDto:
    api = Namespace(name='donation', description="donation 관련 API")
    donation = api.model(
        'donation',
        {
            # 'id': fields.Integer(readonly=True, description="donation 고유 id"),
            'mount': fields.Integer(description="donation 예산 정보"),
            # 'user_id': fields.List(fields.Integer, description="doncation한 User"),
            # 'budget_id': fields.List(fields.Integer, description="donation된 budget 기록"),
        }
    )