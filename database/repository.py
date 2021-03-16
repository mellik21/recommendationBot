import sqlalchemy as db
import config

engine = db.create_engine('sqlite:///' + config.DB_PATH)

connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())