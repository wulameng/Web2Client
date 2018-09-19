import jpush

APP_KEY = '52413f49648130b30cd146b0'
MASTER_SECRET = 'd9a7fb72c088eff6932faf26'
_jpush = jpush.JPush(APP_KEY, MASTER_SECRET)
_jpush.set_logging(True)


class JPushCreate(object):

    def sendMessage(self, command='text', **kwargs):
        push = _jpush.create_push()
        push.audience = jpush.all_
        push.message = jpush.message(command,
                                     extras={'content': kwargs.get('content'), 'toUser': kwargs.get('toUser')})

        push.platform = jpush.platform('android')
        push.send()
