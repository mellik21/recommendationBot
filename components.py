from telebot import types

DEFAULT_MARKUP = None
ASSESSMENT_MARKUP = None
FILM_MARKUP = None
EMPTY_MARKUP = None


def initGlobalMarkup():
    global DEFAULT_MARKUP
    DEFAULT_MARKUP = types.ReplyKeyboardMarkup(resize_keyboard=True)
    DEFAULT_MARKUP.add(types.KeyboardButton('Что посмотреть?'))
    DEFAULT_MARKUP.add(types.KeyboardButton('Уточнить мои интересы'))


def initAssessmentMarkup():
    global ASSESSMENT_MARKUP
    ASSESSMENT_MARKUP = types.InlineKeyboardMarkup()
    ASSESSMENT_MARKUP.add(types.InlineKeyboardButton('Да', callback_data='like'))
    ASSESSMENT_MARKUP.add(types.InlineKeyboardButton('Нет', callback_data='not_like'))


def initFilmMarkup():
    global FILM_MARKUP
    FILM_MARKUP = types.InlineKeyboardMarkup()
    FILM_MARKUP.add(types.InlineKeyboardButton('Возможно позже', callback_data='like'))
    FILM_MARKUP.add(types.InlineKeyboardButton('Точно не буду смотреть', callback_data='not_like'))
    FILM_MARKUP.add(types.InlineKeyboardButton('Уже видел', callback_data='seen'))


def initEmptyMarkup():
    global EMPTY_MARKUP
    EMPTY_MARKUP = types.InlineKeyboardMarkup()


def initDefaultComponents():
    initGlobalMarkup()
    initAssessmentMarkup()
    initFilmMarkup()
    initEmptyMarkup()
