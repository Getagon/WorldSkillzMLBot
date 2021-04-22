#!pip install pytelegrambotapi
#данный код будет сохранён в отдельном скрипт файле для последующего деплоя на Heroku
import telebot
bot = telebot.TeleBot('1765644265:AAFFmVSXp-L3ZFiUp7J62DibhYfjSUxtOaI')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

        bot.polling(none_stop=True)
