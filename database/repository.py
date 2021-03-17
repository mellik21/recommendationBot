import pandas as pd
import sqlalchemy as db

import config

engine = db.create_engine('sqlite:///' + config.DB_PATH)

connection = engine.connect()
metadata = db.MetaData()

studio = db.Table('studio', metadata, autoload=True, autoload_with=engine)
anime = db.Table('anime', metadata, autoload=True, autoload_with=engine)
genre = db.Table('genre', metadata, autoload=True, autoload_with=engine)

query = db.select([studio])
ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()
print(ResultSet[:3])

def load_studios():
    data = pd.read_csv('../files/studios.csv')

    for index, row in data.iterrows():
        query = db.insert(studio).values(id=index, name=row['name'])
        ResultProxy = connection.execute(query)
        
def load_genres():
    data = pd.read_csv('../files/genres.csv')

    for index, row in data.iterrows():
        query = db.insert(genre).values(id=index, name=row['name'])
        ResultProxy = connection.execute(query)
        
        
def load_animes():
    data = pd.read_csv('../files/cleaned_data.csv')
    #TODO изменить структуру таблицы -- удалить дату, добавить год, сезон, время года, серию
    for index, row in data.iterrows():
        query = db.insert(anime).values(id=index, 
                                        page=row['Page'], 
                                        name_rus=row['Rus_name'],
                                        name_eng=row['Eng_name'],
                                        description=row['Description'],
                                        alternative_descriptio=row['Alt_description'],
                                        rating=row['Rating'],
                                        picture_path=row['Img'],
                                        year=row['Year'], #integer
                                        year_season=row['Season'] # создать enum и заодно уточнить что все правильно сохранено
                                        season=row['Season_name'],
                                        seria=row['Seria_name']
                                       )
        ResultProxy = connection.execute(query)
        genres_list = row['Genres']
        for i in range(len(genres_list)):
            query = select(genre).where(genre.name == genres_list[i])
            g = connection.execute(query)
            print(g)

            
        query = db.insert(anime_genres).values(id=index, name=row['name'])
        
