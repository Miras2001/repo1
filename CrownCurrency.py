from typing import Match
from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


print("Bot is displayed")

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id = chat.id, text = "Привет, я конвертер валют!")

def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    try:
        number = float(text)
        rate = 25.42
        crowns = number * rate
        context.bot.send_message(chat_id = chat.id, text=str(crowns) + " крон")
    except:
        context.bot.send_message(chat_id = chat.id, text="Напишите число для перевода")

token = "2107996851:AAE3JQLUOmAfvax4gzUOJ9datUxXRTEpkSk"

updater = Updater(token, use_context="True")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()