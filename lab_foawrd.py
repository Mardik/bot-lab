from telegram.ext import Updater, CommandHandler

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def funcao_handle(update, context):

    #Implemente aqui a função que vai tratar o handler/commando.


updater = Updater('YOUR TOKEN HERE', use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('comando', funcao))

updater.start_polling()
updater.idle()