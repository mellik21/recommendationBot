import telebot
import config as keeper
from telebot import types
import components
from PIL import Image

bot = telebot.TeleBot(keeper.API_TOKEN)
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
            img = open('files/test.jpg', 'rb')
            bot.send_photo(message.chat.id, img, caption='Представьте что рекомендация работает 1 сезон \n⭐ '
                                                         'рейтинг: 9.2 \n Крыс Реми обладает уникальным вкусом. '
                                                         'Он готов рисковать собственной жизнью, чтобы '
                                                         'посмотреть любимое кулинарное шоу и раздобыть '
                                                         'какую-нибудь приправку или просто свежий продукт. '
                                                         'Реми живет со своими сородичами, которые его не '
                                                         'понимают и не принимают его увлечения кулинарией. '
                                                         'Когда Реми случайно попадает на кухню шикарного '
                                                         'ресторана, он решает воспользоваться выпавшим ему '
                                                         'шансом и проверить свои навыки. '
                                                         '', reply_markup=components.FILM_MARKUP)

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
