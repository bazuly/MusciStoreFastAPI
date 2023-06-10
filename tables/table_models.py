from sqlalchemy import Table, Column, String, Float, Integer, TIMESTAMP, JSON, ForeignKey, Boolean, MetaData
from datetime import datetime

metadata = MetaData()

trade_post = Table(
    'trade_post',
    metadata,
    Column('price', Float, nullable=False),
    Column('type', String, nullable=False),
    Column('name', String, nullable=False),
    Column('photo', String, nullable=False)

)

role = Table(
    'role',
    metadata,
    Column('role_id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('permission', JSON)
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('username', String, nullable=False),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.role_id)),
    Column('is_active', Boolean),
    Column('is_superuser', Boolean),
    Column('is_verified', Boolean)
)
