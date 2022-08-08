import telebot
from telebot.types import Message
from config import token

bot = telebot.TeleBot(token)
@bot.message_handler()
def func(message: Message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()