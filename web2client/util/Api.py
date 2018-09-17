from flask import *
from flask_restful import fields, Resource, marshal, marshal_with

from web2client.auth import auth
from web2client.model.GroupSync import *
from web2client.model.MessageSync import *
from web2client.model.PersonSync import *
from web2client.model.NormalResponse import *


class GroupSyncFromClientAPI(Resource):
    result = False
    decorators = [auth.login_required]

    def post(self):
        r = request
        json_data = json.loads(r.data.decode('utf-8'))
        data_len = len(json_data)
        print(data_len)

        if data_len == 0:
            return {"failed": "please commit your http content-type and your posted json data"}, -1
        else:
            for data in json_data:
                with GroupSync(roomid=data.get('roomid'),
                               memberlist=data.get('memberlist'),
                               roomname=data.get('roomname'),
                               roomowner=data.get('roomowner'),
                               modifytime=data.get('modifytime')) as group_node:
                    self.result = sync(group_node)
            if self.result is True:
                return {"success": "success"}, 200
            else:
                return {"failed": "failed"}, -1


class PersonSyncApi(Resource):
    decorators = [auth.login_required]

    def post(self):
        r = request
        json_data = json.loads(r.data.decode('utf-8'))
        data_len = len(json_data)
        print(data_len)
        if json_data is None:
            return {"failed": "post is failed "}, -1
        else:
            for data in json_data:
                with PersonModel(username=data.get('username'),
                                 nickname=data.get('nickname'),
                                 alias=data.get('alias')) as person_node:
                    personSync(person_node)
            return {"success": "person sync success"}


class MessageSyncApi(Resource):
    decorators = [auth.login_required]

    def post(self):
        r = request
        json_data = json.loads(r.data.decode('utf-8'))
        data_len = len(json_data)
        print(data_len)
        if json_data is None:
            return {"failed": "Message Sync failed"}, -1
        else:
            for data in json_data:
                with MessageModel(msgid=data.get('msgid'),
                                  type=data.get('type'),
                                  takler=data.get('takler'),
                                  createtime=data.get('createtime'),
                                  content=data.get('content'),
                                  imagepath=data.get('imagepath')) as message_node:
                    MessageSync(message_node)
            return {"success": "message has been inserted"}


# web 获取所有的会话列表
class SyncChatApi(Resource):

    @marshal_with(fields=NORMAL_RESPONSE)
    def get(self):
        user = ['wdwdwd', 'wdwdwdwd', 12312312412]
        # data = {'rest_desc': 'success', 'rest_code': '200', 'user': ['wx_id', 'asd', 123123]}
        return UserList(rest_code=200, rest_desc='success', user=user)
