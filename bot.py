import telebot

import config
import weather_func

weatherBot = telebot.TeleBot(config.token)


@weatherBot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    weatherBot.reply_to(message, 'Привет, сладкий! Чтобы использовать меня, введи название любого города и я тебе кое-что расскажу...')


@weatherBot.message_handler(func=lambda message: True, content_types=['text'])
def send_forecast(message):
    msg = weather_func.get_weather(message.text)
    print(message.text)
    if msg == None:
        weatherBot.send_message(message.chat.id, 'Введи название существующего города, а не ' + message.text)
    else:    
        weatherBot.send_message(message.chat.id, msg)

if __name__ == '__main__':
    weatherBot.polling(none_stop=True)
