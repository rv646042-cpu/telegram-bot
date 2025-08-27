from telebot import TeleBot, types

# 👇 Yaha apna token paste kar
TOKEN = "8242252445:AAH_NHbTNtxfUNqB6d-AiaqR5QvKNdBPKNg"

bot = TeleBot(TOKEN, parse_mode="HTML")

# Channel join request auto-accept
@bot.chat_join_request_handler()
def join_request(update: types.ChatJoinRequest):
    chat_id = update.chat.id
    user_id = update.from_user.id

    bot.approve_chat_join_request(chat_id, user_id)  # Accept request
    bot.send_message(chat_id, f"✅ Welcome @{update.from_user.username or 'friend'}!")

print("🤖 Bot is running...")
bot.infinity_polling()
