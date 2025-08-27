import telebot

TOKEN = "8242252445:AAH_NHbTNtxfUNqB6d-AiaqR5QvKNdBPKNg"   # apna token paste karo
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot chal raha hai 🚀")

bot.polling()
