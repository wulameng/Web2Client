from datetime import datetime
from peewee import CharField, DateTimeField
from web2client.db.BaseModel import WXBaseModel


class PersonModel(WXBaseModel):
    username = CharField()
    nickname = CharField()
    alias = CharField()
    createtime = DateTimeField()
    updatetime = DateTimeField()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            return True
        else:
            return False

    class Meta:
        db_table = 'tb_person_contact'


def personSync(person_node):
    username = person_node.username
    nickname = person_node.nickname
    alias = person_node.alias
    createtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    count = PersonModel.select().where(PersonModel.username == username).count()

    if count == 0:
        PersonModel.insert(username=username,
                           nickname=nickname,
                           alias=alias,
                           createtime=createtime,
                           updatetime=updatetime).execute()
    else:
        PersonModel.update(nickname=nickname,
                           alias=alias,
                           updatetime=updatetime).where(PersonModel.username == username).execute()
