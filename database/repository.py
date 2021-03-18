import pandas as pd
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from model.Anime import Anime
from model.Genre import Genre
import config

engine = db.create_engine(config.USER_DB_CONF)
connection = engine.connect()

metadata = db.MetaData()
studio = db.Table('studio', metadata, autoload=True, autoload_with=engine)
anime = db.Table('anime', metadata, autoload=True, autoload_with=engine)
genre = db.Table('genre', metadata, autoload=True, autoload_with=engine)
anime_genre = db.Table('anime_genre', metadata, autoload=True, autoload_with=engine)


def get_anime_by_id(id) -> Anime:
    query = db.select([anime]).where(anime.columns.id == id)
    result = connection.execute(query)
    for row in result:
        #  query = db.select([anime_genre.columns.genre_id, genre.columns.id]).where(anime_genre.columns.anime_id == row['id'])
        #  query = (anime_genre,genre).filter, genre.columns.id == anime_genre.columns.genre_id))
     #   result = connection.execute(anime_genre, genre)\
     #     .filter(anime_genre.genre_id == genre.id)\
     #       .filter(anime_genre.anime_id == id)\
      #      .all()
        result = connection.execute('select fr')

        s_genres = []
        for r in result:
            # g = Genre(
            #       id=r['id'],
            #      name_rus=r['name_rus'],
            #      name_eng=""
            #   )
            print(r)
            s_genres.append(r['name_rus'])

        return Anime(
            id=row['id'],
            page=row['page'],
            name_rus=row['name_rus'],
            name_eng=row['name_eng'],
            description=row['description'],
            alt_description=row['alternative_description'],
            rating=row['rating'],
            picture_path=row['picture_path'],
            release_year=row['release_year'],
            year_season=row['year_season'],
            season=row['season'],
            seria=row['seria'],
            genres=str(s_genres),
            minor_names="",
            studio=''
        )


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

    # load_anime_studios()
