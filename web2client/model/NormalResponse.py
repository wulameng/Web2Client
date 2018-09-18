from flask_restful import fields

USER_LIST = {
    'wx_id': fields.String(),
    'nick_name': fields.String(),
    'last_message_time': fields.DateTime()
}

NORMAL_RESPONSE = {'rest_desc': fields.String,
                   'rest_code': fields.Integer,
                   'user': fields.List(fields.Nested(USER_LIST))
                   }
NEW_MESSAGE = {
    'content': fields.String(),
    'message_time': fields.String(),
    'talker': fields.String(),
    'to_user': fields.String(),
    'message_type': fields.Integer()
}
MESSAGE_RESPONSE = {'rest_desc': fields.String(),
                    'rest_code': fields.Integer(),
                    'message': fields.List(fields.Nested(NEW_MESSAGE))
                    }


class MessageList(object):
    def __init__(self, rest_desc, rest_code, message=None):
        self.rest_desc = rest_desc
        self.rest_code = rest_code
        self.message = message


class Message(object):
    def __init__(self, content, message_time, talker, to_user, message_type):
        self.content = content
        self.message_type = message_type
        self.message_time = message_time
        self.to_user = to_user
        self.talker = talker


class UserList(object):

    def __init__(self, rest_desc, rest_code, user):
        self.rest_desc = rest_desc
        self.rest_code = rest_code
        self.user = user


class User(object):

    def __init__(self, wx_id, nick_name, last_message_time):
        self.wx_id = wx_id
        self.nick_name = nick_name
        self.last_message_time = last_message_time
