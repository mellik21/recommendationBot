import datetime
import pytz


def get_now_formatted() -> str:
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    return now.strftime("%Y-%m-%d %H:%M:%S")
