from telegram.ext import Updater, CommandHandler
from decouple import config

TOKEN = config('TOKEN')

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

# Função de tramento de comando
# Retorna o ID do usuário;
def get_id(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Pega o ID do usuário que chamou o comando;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada;
    #from_user: equivale "from" do mensagem com dados do usuário que enviou;
    #id: é o dado do usuário, no caso o ID dele;  
    update.message.reply_text(
        'Seu ID é {}'.format(update.message.from_user.id))

# Retorna uma mensagem de boas vindas;
def hello(update, context):
    #Menda uma mensagem de hello;
    update.message.reply_text(
        'Hello my friendy!!')

# Manda uma mensagem com link do site do grupo;
def site(update, context):
    update.message.reply_text(
        'Espero que goste do nosso site: https://devopspbs.org/')

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('getid', get_id))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('site', site))

updater.start_polling()
updater.idle()