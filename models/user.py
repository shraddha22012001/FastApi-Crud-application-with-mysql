from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table,Column
from config.db import meta
users = Table(
    'users',meta,
    Column('id',Integer,primary_key = True),
    Column('name',String(255)),
    Column('phone',String(255)),
    Column('email',String(255)),

)