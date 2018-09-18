from web2client.db.BaseModel import WXBaseModel
from peewee import CharField, BigIntegerField, IntegerField, DateTimeField


class MessageModel(WXBaseModel):
    msgid = BigIntegerField()
    type = IntegerField()
    takler = CharField()
    createtime = DateTimeField()
    content = CharField()
    imagepath = CharField()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            return True
        else:
            return False

    class Meta:
        db_table = 'tb_message_model'


def MessageSync(message_node):
    msgid = message_node.msgid
    type = message_node.type
    takler = message_node.takler
    createtime = message_node.createtime
    content = message_node.content
    imagepath = message_node.imagepath
    MessageModel.insert(msgid=msgid, type=type,
                        takler=takler,
                        createtime=createtime,
                        content=content,
                        imagepath=imagepath).execute()



