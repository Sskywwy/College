import telebot

bot = telebot.TeleBot('7875954840:AAGCw_-aOR0ZVti3wEUvxFSaoKJCY7FL918', parse_mode=None)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
