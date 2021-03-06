import datetime
import pytz


def get_now_formatted() -> str:
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    return now.strftime("%Y-%m-%d %H:%M:%S")


def appendTextOrAttr(value, list, attr=None):
    if value is not None:
        if attr is not None:
            list.append(value[attr])
        else:
            list.append(value.text)
    else:
        list.append("")
