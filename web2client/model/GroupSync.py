from peewee import CharField, DateTimeField

from web2client.db.BaseModel import *


class GroupSync(WXBaseModel):
    roomid = CharField()
    memberlist = CharField()
    roomname = CharField()
    roomowner = CharField()
    modifytime = DateTimeField()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            return True
        else:
            return False

    class Meta:
        db_table = 'tb_web2client_group'


def sync(group_node):
    roomid = group_node.roomid
    memberlist = group_node.memberlist
    roomname = group_node.roomname
    roomowner = group_node.roomowner
    modifytime = group_node.modifytime
    num = GroupSync.select().where(GroupSync.roomid == roomid).count()
    if num == 1:
        GroupSync.update(memberlist=memberlist,
                         roomname=roomname,
                         roomowner=roomowner,
                         modifytime=modifytime).where(GroupSync.roomid == roomid).execute()
        return True
    elif num == 0:
        GroupSync.insert(roomid=roomid,
                         memberlist=memberlist,
                         roomname=roomname,
                         roomowner=roomowner,
                         modifytime=modifytime).execute()
        return True
