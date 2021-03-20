import database.db_helper as db
import models


def get_anime_by_id(id) -> models.Anime:
    animes = db.get_by_id("anime", models.anime_columns, id)
    genres = db.get_genres_by_anime_id(id)
    s_genres = []
    for genre in genres:
        s_genres.append(genre[0])

    finded = None
    for anime in animes:
        finded = models.Anime(
            id=anime[0],  # 'id'
            page=anime[1],  # 'page'
            name_rus=anime[2],  # 'name_rus'
            name_eng=anime[3],  # 'name_eng'
            description=anime[4],  # 'description'
            alt_description=anime[5],  # 'alternative_description'
            rating=anime[6],  # 'rating'
            picture_path=anime[7],  # 'picture_path'
            release_year=anime[8],  # 'release_year'
            year_season=anime[9],  # 'year_season'
            season=anime[10],  # 'season'
            seria=anime[11],  # 'seria'
            genres=s_genres,
            minor_names=[],
            studio=[]
        )

    return finded

# cursor.execute(
#      "select e.id, e.amount, c.name "
#      "from expense e left join category c "
#     "on c.codename=e.category_codename "
#      "order by created desc limit 10")
