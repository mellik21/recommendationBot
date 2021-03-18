import pandas as pd
import sqlalchemy as db
from sqlalchemy.dialects import mysql

import config

engine = db.create_engine(config.USER_DB_CONF)
connection = engine.connect()

metadata = db.MetaData()
studio = db.Table('studio', metadata, autoload=True, autoload_with=engine)
anime = db.Table('anime', metadata, autoload=True, autoload_with=engine)
genre = db.Table('genre', metadata, autoload=True, autoload_with=engine)
anime_genre = db.Table('anime_genre', metadata, autoload=True, autoload_with=engine)


def drop_table(s):
    metadata.drop_all(engine, [s], checkfirst=True)


def execute(s):
    return connection.execute(s)


def table_names():
    print(engine.table_names())


def load_studios():
    data = pd.read_csv('../files/studios.csv')
    for index, row in data.iterrows():
        connection.execute(db.insert(studio).values(id=index, name=row['name']))


def load_genres():
    data = pd.read_csv('../files/genres.csv')
    for index, row in data.iterrows():
        connection.execute(db.insert(genre).values(id=index, name_rus=row['name']))


def load_animes():
    data = pd.read_csv('../files/not_none_cleaned_data.csv')
    for index, row in data.iterrows():
        query = anime.insert().values(id=index,
                                      page=row['Page'],
                                      name_rus=row['Rus_name'],
                                      name_eng=row['Eng_name'],
                                      description=row['Description'],
                                      alt_description=row['Alt_description'],
                                      rating=row['Rating'],
                                      picture_path=row['Img'],
                                      release_year=row['Year'],
                                      year_season=row['Season'],
                                      season=row['Season_name'],
                                      seria=row['Seria_name']
                                      )

        result = connection.execute(query)
        new_id = result.inserted_primary_key
        print(new_id)
        genres = row['Genres'].replace('[', '').replace(']', '')
        for genre in genres.split(','):
            query = anime_genre.insert().values(genre_id=int(genre.strip()), anime_id=new_id)
            connection.execute(query)


load_animes()
