from telegram.ext import Updater, CommandHandler
from decouple import config

TOKEN = config('TOKEN')

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def site(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Menda uma mensagem com link do site do grupo;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    update.message.reply_text(
        'Espero que goste do nosso site:\n https://devopspbs.org/')

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('site', site))

updater.start_polling()
updater.idle()