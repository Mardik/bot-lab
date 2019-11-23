from telegram.ext import Updater, CommandHandler

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def funcao(update, context):

    #Envia uma mensagem com o conteúdo passado como parametro.
    update.message.reply_text(
        'Menssagem {}'.format(update.message.from_user.first_name))


updater = Updater('YOUR TOKEN HERE', use_context=True)

#Vincula função a comando
updater.dispatcher.add_handler(CommandHandler('comando', funcao))

updater.start_polling()
updater.idle()