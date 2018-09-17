from flask_restful import fields

USER_LIST = {
    'wx_id': fields.String(),
    'nick_name': fields.String(),
    'last_message_time': fields.Integer()
}

NORMAL_RESPONSE = {'rest_desc': fields.String,
                   'rest_code': fields.Integer,
                   'user': fields.List(fields.Nested(USER_LIST))
                   }


class UserList(object):

    def __init__(self, rest_desc, rest_code, user):
        self.rest_desc = rest_desc
        self.rest_code = rest_code
        self.user = user
