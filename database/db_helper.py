import os
from typing import Dict, List, Tuple
import config
# import mysql.connector as cn
import pymysql

# conn = mysql.connector.connect(config.MYSQL_DB_CONFIG)
# conn = cn.connect(config.host, config.user, config.password, config.database)


conn = pymysql.connect(config.host, config.user, config.password, config.database)
cursor = conn.cursor()


def get_by_id(table: str, columns: str, id: int) -> List[Tuple]:
    print('SELECT ' + columns + ' FROM ' + table + ' WHERE id = ' + str(id))
    cursor.execute(
        f"SELECT {columns} FROM {table} WHERE id ={id} "
    )
    return cursor.fetchall()


def get_genres_by_anime_id(id: int) -> List[Tuple]:
    print(
        'SELECT name_rus FROM anime_genre inner join genre on genre.id = anime_genre.genre_id WHERE anime_id = ' + str(
            id))
    cursor.execute(
        f"SELECT name_rus FROM anime_genre inner join genre on genre.id = anime_genre.genre_id "
        f"WHERE anime_id ={id}"
    )
    return cursor.fetchall()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    print('f"SELECT {' + columns_joined + '} FROM {' + table + '}')
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def _init_db():
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='category'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()
