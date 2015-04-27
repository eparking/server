from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
spot = Table('spot', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('location', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
    Column('vacancy', INTEGER),
    Column('Field6', INTEGER),
)

spot = Table('spot', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location', String(length=140)),
    Column('timestamp', DateTime),
    Column('vacancy', Integer),
    Column('owner_id', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['spot'].columns['Field6'].drop()
    post_meta.tables['spot'].columns['owner_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['spot'].columns['Field6'].create()
    post_meta.tables['spot'].columns['owner_id'].drop()
