import os
from datetime import datetime

from decouple import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Configuration
CHAT_ID = '-310613930'
TOKEN = config('TOKEN')
FORWARD = range(1)


def start(update, context):
    text = 'Hello {}'.format(update.message.from_user.first_name)
    update.message.reply_text(text)
    context.bot.send_message(chat_id='26072030', text=text)
    print(text)


def get_id(update, context):
    text = 'Seu id é {}'.format(update.message.chat.id)
    update.message.reply_text(text)


def data_hora(update, context):
    text = str(datetime.now())
    print(text)
    update.message.reply_text(text)


def firefox_open(update, context):
    os.system('firefox')
    update.message.reply_text('Ok entendi sua solicitação e estou abrindo o firefox')


def contact(update, context):
    update.message.reply_text('Ok, send your question please.')
    return FORWARD


def forward(update, context):
    update.message.forward(chat_id=CHAT_ID)


def answer(update, context):
    chat_id = update.message.reply_to_message.forward_from.id
    text = update.message.text
    context.bot.send_message(chat_id=chat_id, text=text)


def any_message(update, context):
    print(update)


updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(ConversationHandler(
    entry_points=[CommandHandler('contact', contact)],
    states={FORWARD: [MessageHandler(Filters.text, forward)], },
    fallbacks=[CommandHandler('start', start)]))

dp.add_handler(CommandHandler('getid', get_id))
dp.add_handler(CommandHandler('hello', start))
dp.add_handler(CommandHandler('firefox', firefox_open))
dp.add_handler(CommandHandler('now', data_hora))
dp.add_handler(CommandHandler('tempo', 'tempo', pass_args=True))

dp.add_handler(MessageHandler(Filters.reply, answer))
dp.add_handler(MessageHandler(Filters.update, any_message))

updater.start_polling()
updater.idle()
