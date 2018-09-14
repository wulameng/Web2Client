from flask import render_template
from . import chat_blue


@chat_blue.route("/chat.html")
def chat():
    user = {'nickname', 'mike'}
    return render_template('index.html', title='HOMEPAGE', user=user)

