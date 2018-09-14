from flask import Blueprint
chat_blue = Blueprint('chat', __name__)
from web2client.chat import views
