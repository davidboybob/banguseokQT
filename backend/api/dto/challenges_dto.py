from flask_restx import Namespace, fields

class ChallengesDto:
    api = Namespace(name='challenges', description="Challenges 관련 API")
    challenges = api.model(
        'challenges',
        {
            # 'id': fields.Integer(readonly=True, description="Challengs 고유 id"),
            'state': fields.Boolean(description="Challenges 진행 여부 상태 Boolean 값"),
            'title': fields.String(required=True, description="Challenges 제목"),
            'contents': fields.String(required=True, description="Challenges 내용"),
            'from_date': fields.DateTime(required=True, description="Challenges 시작 일자"),
            'to_date': fields.DateTime(required=True, description="Challenges 종료 일자"),

            # 'user_id': fields.List(fields.Integer, description="Challenges에 속한 User"),
            # 'qt_id': fields.List(fields.Integer, description="Challenges에 속한 Qt"),
            # 'budget_id': fields.List(fields.Integer, description="Challenges에 속한 Budget"),
        }
    )