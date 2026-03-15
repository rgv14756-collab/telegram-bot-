import telebot

TOKEN = '8792226891:AAHq5cTfbdGVf7QPlugEAnN1WhES3t_jDa8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, "Бот запущен и работает!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

if __name__ == '__main__':
    print("Бот пошел в работу...")
    bot.infinity_polling()
