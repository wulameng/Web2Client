import jpush

APP_KEY = '07e60f46ead68a3388de8f81'
MASTER_SECRET = '88c91a21f91c4bbe8a9b4f6b'
_jpush = jpush.JPush(APP_KEY, MASTER_SECRET)
_jpush.set_logging(True)


# PUSH_MODEL = {
#     'command':
# }

class JPushCreate(object):

    def sendMessage(self, command='text', **kwargs):
        push = _jpush.create_push()
        push.audience = jpush.all_

        if command == 'text':
            push.message = jpush.message(command,
                                         extras={'content': kwargs.get('content'), 'toUser': kwargs.get('toUser')})
        else:
            push.message = jpush.message(command, extras={'k2': 'v2', 'k3': 'v3'})
        push.platform = jpush.platform('android')
        push.send()
