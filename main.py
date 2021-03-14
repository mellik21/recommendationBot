import telebot
import config as keeper
from telebot import types
import components

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
            bot.send_message(message.chat.id, "")
        elif message.text == 'Уточнить мои интересы':
            bot.register_next_step_handler(bot.send_message(message.chat.id,
                                                            "Введите название любимого аниме. "
                                                            "Мы исключим его из рекомендаций и скорректируем ваши предпочтения!"),
                                           search)


def search(message):
    bot.send_message(message.chat.id, "Закройте глаза и представьте что поиск работает. Мы угадали?",
                     reply_markup=components.ASSESSMENT_MARKUP)


components.initDefaultComponents()
bot.polling(none_stop=True)
