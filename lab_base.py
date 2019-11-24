from decouple import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = config('TOKEN')


def start(update, context):
    update.message.reply_text('{} já estou funcionando.'.format(
        update.message.from_user.first_name))


def function(update, context):
    # Função de tramento de comando
    #Envia uma mensagem com o conteúdo passado como parametro.
    update.message.reply_text(
        '{} sua função foi executada.'.format(update.message.from_user.first_name))


def message(update, context):
    update.message.reply_text(
        '{} você me enviou a mensagem {}.'.format(
            update.message.from_user.first_name,
            update.message.text))


updater = Updater(TOKEN, use_context=True)
"""
Fornece um frontend para class: `telegram.Bot` para o programador, 
para que ele possa se concentrar na codificação do bot. Seu objetivo é
receber as atualizações do Telegram e entregá-las ao referido manipulador.
"""
dp = updater.dispatcher
"""
Essa classe despacha todos os tipos de atualizações para seus manipuladores registrados.
"""

#Vincula função a comando
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('comando', function))
"""
add_handler = Registrar um manipulador
ComandHandler(command, callback) = 
Classe de manipulador para manipular comandos do Telegram.
"""

dp.add_handler(MessageHandler(Filters.update, message))
"""
MessageHandler(filters, callback) = 
Classe para manipular mensagens. Podem conter atualizações de texto, mídia ou status.
"""

updater.start_polling()
updater.idle()
