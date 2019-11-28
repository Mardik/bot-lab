from telegram.ext import Updater, CommandHandler
from decouple import config
import datetime

TOKEN = config('TOKEN')

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def now(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Menda uma mensagem com data e hora;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    update.message.reply_text(
        datetime.datetime.now().strftime('Agora são %H:%S, %d %b %Y'))

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('now', now))

updater.start_polling()
updater.idle()

