import telebot

TOKEN = "8242252445:AAH_NHbTNtxfUNqB6d-AiaqR5QvKNdBPKNg"
bot = telebot.TeleBot(TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot chal raha hai 🚀")

# /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Commands:\n/start - Bot start karo\n/help - Help lo\n/about - Bot ke baare me")

# /about command
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Ye ek demo Telegram bot hai, jo Python me bana hai 🐍")

bot.polling()
