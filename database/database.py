import os
from typing import Dict, List, Tuple
import sqlite3
import config as keeper

conn = sqlite3.connect(os.path.realpath(keeper.DB_PATH), check_same_thread=False)
cursor = conn.cursor()


def select_by_column(table: str, columns: List[str], column: str, value: int) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table} WHERE {column}={value}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def update(table: str, column_values: Dict, row_id: int):
    statement = " "
    for key in column_values.keys():
        statement = ', '.join(key + " = " + "?" * len(column_values[key]))

    cursor.executemany(
        f"UPDATE {table} "
        f"SET {statement} "
        f"WHERE (id = {row_id})",
        column_values.values())
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


check_db_exists()
