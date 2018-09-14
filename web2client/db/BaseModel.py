import os

from peewee import Model
from playhouse.pool import PooledMySQLDatabase

# environment = os.environ.get('WECHAT2BOT')
# if environment == 'online':
#     from .online_db_config import *
# else:
from .test_db_config import *

mysqlDB = PooledMySQLDatabase(
    host=HOST,
    port=PORT,
    database=DBNAME,
    user=USERNAME,
    passwd=PASSWORD,
    charset=CHARSET,
    max_connections=None,
    connect_timeout=300,
    stale_timeout=300)


class WXBaseModel(Model):
    class Meta:
        database = mysqlDB
