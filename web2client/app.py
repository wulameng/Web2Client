# coding: utf-8
from flask import Flask
from flask_restful import Api

from web2client.chat import chat_blue
from web2client.util.Api import *

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(chat_blue, url_prefix='/chat')
from web2client import view

api = Api(app)
api.add_resource(MessageSyncApi, '/postMessage', endpoint='postMessage')
api.add_resource(GroupSyncFromClientAPI, '/postGroup', endpoint='postGroup')
api.add_resource(PersonSyncApi, '/postPerson', endpoint='postPerson')
api.add_resource(SyncContactApi, '/getContact', endpoint='getContact')
api.add_resource(SendMessageApi, '/sendMessage', endpoint='sendMessage')


@app.before_request
def connect_db():
    print('connect to database')
    if mysqlDB.is_closed():
        mysqlDB.connect()


@app.teardown_request
def close_db(sel):
    print('close to connect database')
    if not mysqlDB.is_closed():
        mysqlDB.close()
