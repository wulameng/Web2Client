import threading

from flask import *
from flask_restful import Resource, marshal_with
from web2client.auth import auth
from web2client.model.GroupSync import *
from web2client.model.MessageSync import *
from web2client.model.PersonSync import *
from web2client.model.NormalResponse import *
from web2client.util.PushUtil import JPushCreate
from web2client.util.IMessage import *


class GroupSyncFromClientApi(Resource):
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


class MessageSyncApi(Resource, IMessage):
    decorators = [auth.login_required]
    new_message_list = []
    obs = []

    def attach(self, ob):
        if ob not in self.obs:
            self.obs.append(ob)

    def detach(self, ob):
        if ob in self.obs:
            self.obs.remove(ob)

    def notify(self, list):
        for ob in self.obs:
            ob.update(list)

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
                    new_message = Message(content=message_node.content, message_time=message_node.createtime,
                                          talker=message_node.takler, to_user='',
                                          message_type=message_node.type)
                    self.new_message_list.append(new_message)
            self.notify(list=self.new_message_list)
            return {"rest_code": 200, "rest_desc": "message has been inserted"}, 200


# web 获取所有的会话列表
class SyncContactApi(Resource):
    decorators = [auth.login_required]
    user_list = []

    @marshal_with(fields=NORMAL_RESPONSE)
    def get(self):
        query = PersonModel.select(PersonModel.username, PersonModel.nickname,
                                   PersonModel.updatetime).order_by(PersonModel.updatetime.desc()).limit(20)
        for cursor in query:
            self.user_list.append(
                User(nick_name=cursor.username, wx_id=cursor.username,
                     last_message_time=cursor.updatetime))
        if len(self.user_list) == 0:
            return UserList(rest_code=-1, rest_desc='failed', user=None)
        else:
            return UserList(rest_code=200, rest_desc='success', user=self.user_list)


# last api
class SyncChatApi(Resource, Observer):
    decorators = [auth.login_required]
    condition = threading.Condition()
    arg_list = []

    def __init__(self):
        MessageSyncApi().attach(self)

    def update(self, list):
        self.arg_list = list
        self.condition.acquire()
        self.condition.notifyAll()
        self.condition.release()
        return

    @marshal_with(fields=MESSAGE_RESPONSE)
    def get(self):
        self.condition.acquire()
        self.condition.wait(25)
        if len(self.arg_list) == 0:
            return MessageList(rest_desc='stop thread', rest_code=-1)
        else:
            # json_data = json.dumps(self.arg_list, default=NEW_MESSAGE)
            # print(json_data)
            return MessageList(rest_code=200, rest_desc='success', message=self.arg_list)


class SendMessageApi(Resource):
    decorators = [auth.login_required]
    content = ''
    to_user = ''

    def post(self):
        r = request
        json_data = json.loads(r.data.decode('utf-8'))
        data_len = len(json_data)
        print(data_len)

        self.content = json_data.get('content')
        self.to_user = json_data.get('toUser')
        if self.content is not None and self.to_user is not None:
            JPushCreate().sendMessage(command='text', content=self.content, toUser=self.to_user)
            return {'rest_desc': 'success', 'rest_code': 200}, 200
        else:
            return {'rest_desc': 'content or toUser is None', 'rest_code': -1}, -1
