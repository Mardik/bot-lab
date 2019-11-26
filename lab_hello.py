from telegram.ext import Updater, CommandHandler
from decouple import config

TOKEN = config('TOKEN')

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def hello(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Menda uma mensagem de hello;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    update.message.reply_text(
        'Hello my friendy!!')

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()