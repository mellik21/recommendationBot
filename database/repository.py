import pandas as pd
import sqlalchemy as db

import config

engine = db.create_engine('sqlite:///' + config.DB_PATH)

connection = engine.connect()
metadata = db.MetaData()

studio = db.Table('studio', metadata, autoload=True, autoload_with=engine)
query = db.select([studio])
ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()
print(ResultSet[:3])


def load_studios():
    data = pd.read_csv('../files/studios.csv')

    for index, row in data.iterrows():
        query = db.insert(studio).values(id=index, name=row['name'])
        ResultProxy = connection.execute(query)
