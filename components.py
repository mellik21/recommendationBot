from telebot import types

DEFAULT_MARKUP = None
ASSESSMENT_MARKUP = None
FILM_MARKUP = None


def initGlobalMarkup():
    global DEFAULT_MARKUP
    DEFAULT_MARKUP = types.ReplyKeyboardMarkup(resize_keyboard=True)
    DEFAULT_MARKUP.add(types.KeyboardButton('Что посмотреть?'))
    DEFAULT_MARKUP.add(types.KeyboardButton('Уточнить мои интересы'))


def initAssessmentMarkup():
    global ASSESSMENT_MARKUP
    ASSESSMENT_MARKUP = types.InlineKeyboardMarkup()
    ASSESSMENT_MARKUP.add(types.InlineKeyboardButton('Да', callback_data='yes'))
    ASSESSMENT_MARKUP.add(types.InlineKeyboardButton('Нет', callback_data='no'))


def initFilmMarkup():
    global FILM_MARKUP
    FILM_MARKUP = types.InlineKeyboardMarkup()
    FILM_MARKUP.add(types.InlineKeyboardButton('Информация', callback_data='info'))
    FILM_MARKUP.add(types.InlineKeyboardButton('Нравится', callback_data='like'))
    FILM_MARKUP.add(types.InlineKeyboardButton('Не нравится', callback_data='not_like'))
    FILM_MARKUP.add(types.InlineKeyboardButton('Уже смотрел', callback_data='seen'))


def initDefaultComponents():
    initGlobalMarkup()
    initAssessmentMarkup()
    initFilmMarkup()
