from telegram.ext import Updater, CommandHandler
from decouple import config

TOKEN = config('TOKEN')

#Updater - Dados novos enviados
#CommandHandler - Instância de um comando.

#Função de tramento de comando
def links(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Manda uma mensagem com links importante do grupo e de outras comunidades;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    update.message.reply_text(
        """
        Lista de link's importantes do grupo:
        # Comunidade DevOpsPBS
        Site: https://devopspbs.org/
        Telegram:
        Meetup: https://www.meetup.com/pt-BR/devopspbs/?action=join
        # Comunidade Tecnologia CKS
        Whatsapp:https://chat.whatsapp.com/JDs2EaIh4enKFMuuYKHsYE
        # Comunidade ArduinoPBS
        Facebook: http://fb.com/ArduinoParauapebas
        YouTube: http://bit.ly/2HuphiY
        WhatsApp: http://bit.ly/2JofD3q
        # Power BI
        MeetUp: https://www.meetup.com/PowerBI-Carajas/
        """
        )

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('links', links))

updater.start_polling()
updater.idle()