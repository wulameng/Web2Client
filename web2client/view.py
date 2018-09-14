from flask import render_template, flash, redirect
from web2client.app import app
from web2client.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/chat/chat.html')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
