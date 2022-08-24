from flask_restx import Namespace, fields

class UserDto:
    api = Namespace(name='user', description='User 정보 관련 API')
    user = api.model(
        'user',
        {
            'id': fields.Integer(readonly=True, description="User 고유 id"),
            'name': fields.String(required=True, description="User 이름"),
            'email': fields.String(required=True, description="User 이메일, 아이디로 사용"),
            'password': fields.String(required=True, description="User 암호화된 비밀번호"),
            'public_id': fields.String(description="User Identifier(Id)"),
            'own_donations_mount': fields.Integer(description="User 후원금"),
            # 'created_at': fields.DateTime(description="User 생성 일자"),
            # 'updated_at': fields.DateTime(description="User 생성 일자"),
            
            'qt_id': fields.List(fields.Integer, description="User Qt 리스트"),
            'commnets_id': fields.List(fields.Integer, description="User 댓글 리스트"),
            'challenges_id': fields.List(fields.Integer, description="User 챌린지 리스트"),
            'donation_id': fields.List(fields.Integer, description="User 도네이션 리스트"),
        }
    )

class QtDto:
    api = Namespace(name='qt', description='Qt 정보 관련 API')
    qt = api.model(
        'qt',
        {
            'id': fields.Integer(readonly=True, description= "Qt 고유 id"),
            'blog_url': fields.String(description="블로그 URL"),
            'title': fields.String(description="QT 제목"),
            'contents': fields.String(description="QT 내용"),

            'user_id': fields.List(fields.Integer, description="Qt 작성한 User 정보"),
            'comments_id': fields.List(fields.Integer, description="Qt에 작성된 Commencts"),
            'challenges_id': fields.List(fields.Integer, description="Qt가 속한 Challenges"),
        }
    )
    # print(UserDto.user.get('name'))

class CommentsDto:
    api = Namespace(name='comments', description="Comments 관련 API")
    comments = api.model(
        'comments',
        {
            'id': fields.Integer(readonly=True, description= "Comments 고유 id"),
            'contents': fields.String(requried=True, description="댓글 내용"),

            'user_id': fields.List(fields.Integer, description="Comments를 작성한 User"),
            'qt_id': fields.List(fields.Integer, description="Comments가 속한 Qt "),
        }
    )

class ChallengesDto:
    api = Namespace(name='challenges', description="Challenges 관련 API")
    challenges = api.model(
        'challenges',
        {
            'id': fields.Integer(readonly=True, description="Challengs 고유 id"),
            'state': fields.Boolean(description="Challenges 진행 여부 상태 Boolean 값"),
            'title': fields.String(required=True, description="Challenges 제목"),
            'contents': fields.String(required=True, description="Challenges 내용"),
            'from_date': fields.DateTime(required=True, description="Challenges 시작 일자"),
            'to_date': fields.DateTime(required=True, description="Challenges 종료 일자"),

            'user_id': fields.List(fields.Integer, description="Challenges에 속한 User"),
            'qt_id': fields.List(fields.Integer, description="Challenges에 속한 Qt"),
            'budget_id': fields.List(fields.Integer, description="Challenges에 속한 Budget"),
        }
    )

class BudgetDto:
    api = Namespace(name='budget', description="budget 관련 API")
    budget = api.model(
        'budget',
        {
            'id': fields.Integer(readonly=True, description="budget 고유 id"),
            'mount': fields.Integer(description="budget 예산 정보"),
            'donation_id': fields.List(fields.Integer, description="budget donation id"),
            'challenges_id': fields.List(fields.Integer, description="budget challenges 이전비")
        }
    )

class DonationDto:
    api = Namespace(name='donation', description="donation 관련 API")
    donation = api.model(
        'donation',
        {
            'id': fields.Integer(readonly=True, description="donation 고유 id"),
            'mount': fields.Integer(description="donation 예산 정보"),
            'user_id': fields.List(fields.Integer, description="doncation한 User"),
            'budget_id': fields.List(fields.Integer, description="donation된 budget 기록"),
        }
    )