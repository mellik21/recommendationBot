from random import randrange
import telebot
from telebot import types
import components
from PIL import Image
import database.repository as rep
import requests
import config

bot = telebot.AsyncTeleBot(config.API_TOKEN)
defaultMarkup = None


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЭтот бот поможет тебе найти аниме для просмотра! '
                     .format(message.from_user),
                     parse_mode='html', reply_markup=components.DEFAULT_MARKUP)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.type == 'private':
        if message.text == 'Что посмотреть?':
            rand_anime_id = randrange(1916)
            anime = rep.get_anime_by_id(rand_anime_id)
            print(anime)
            print(config.BASE_URL + anime.picture_path)
            img = Image.open(requests.get(config.BASE_URL + anime.picture_path, stream=True).raw)

            text = anime.name_rus + '\n⭐ рейтинг:' + str(anime.rating) + '\n ' + anime.description
            bot.send_photo(message.chat.id, img, caption=text, reply_markup=components.FILM_MARKUP)

        elif message.text == 'Уточнить мои интересы':
            bot.register_next_step_handler(
                bot.send_message(message.chat.id,
                                 "Введите название любимого аниме. "
                                 "Мы исключим его из рекомендаций "
                                 "и скорректируем ваши предпочтения!"), search)


def search(message):
    bot.send_message(message.chat.id, "Закройте глаза и представьте что поиск работает. Мы угадали?",
                     reply_markup=components.ASSESSMENT_MARKUP)


@bot.callback_query_handler(func=lambda call: call.data in ['like', 'not_like'])
def callback_inline_assessments(call):
    message = call.message
    if message:
        #   if call.data == 'like':
        # else call.data == 'not_like':
        if message.caption is not None:
            bot.edit_message_caption(chat_id=message.chat.id, message_id=message.message_id, caption=message.caption,
                                     reply_markup=components.EMPTY_MARKUP)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=message.text,
                                  reply_markup=components.EMPTY_MARKUP)

        bot.send_message(message.chat.id, "Обязательно учтем это!")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_assessments(call):
    message = call.message
    if message:
        if call.data == 'seen':
            bot.edit_message_caption(chat_id=message.chat.id, message_id=message.message_id, caption=message.caption,
                                     reply_markup=components.EMPTY_MARKUP)
            bot.send_message(message.chat.id, "Ого, здорово! Понравилось?", reply_markup=components.ASSESSMENT_MARKUP)


components.initDefaultComponents()
bot.polling(none_stop=True)
