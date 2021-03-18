from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.schema import ForeignKey

class Anime(Base):
    __tablename__ = 'anime'
    id = Column(Integer(), primary_key=True)
    name_rus = Column(String())
    name_eng = Column(String())
    page = Column(Integer())
    description = Column(String())
    alt_description = Column(String())
    studio = Column(String())
    rating = Column(Float())
    picture_path = Column(String())
    release_year = Column(Integer())
    year_season = Column(String())
    season = Column(String())
    seria = Column(String())
    genres = Column(String())
    minor_names = Column(String())


class AnimeGenre(Base):
    __tablename__ = 'anime_genre'
    name = Column(String, primary_key=True)
    author = Column(String, ForeignKey("users.email"))


class Genre(Base):
    __tablename__ = 'genre'
    readAllowed = Column(Boolean)
    writeAllowed = Column(Boolean)

    document = Column(String, ForeignKey("documents.name"))
