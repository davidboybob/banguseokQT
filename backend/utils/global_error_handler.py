def create_error_handler(api):
    @api.errorhandler(Exception)
    def handle_all_exception(error):
        print(error)
        code = 500
        data = {'status': 'error', 'message': '알수없는 에러가 발생했습니다.'}
        if hasattr(error, "code"):
            code = error.code
            data = error.data
        return data, code