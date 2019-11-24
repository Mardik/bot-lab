import os
from decouple import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = config('TOKEN')


def start(update, context):
    update.message.reply_text('{} já estou funcionando.'.format(
        update.message.from_user.first_name))


def open_firefox(update, context):
    update.message.reply_text(
        '{} recebi seu comoando e vou abrir o firefox agora.'.format(
            update.message.from_user.first_name))
    os.system('firefox')


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('firefox', open_firefox))

updater.start_polling()
updater.idle()
