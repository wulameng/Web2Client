from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'syncmanager':
        return 'fittime1991'
    return None
