from telegram.ext import Updater, CommandHandler
from decouple import config
from collections import namedtuple
import datetime
import json
import requests

TOKEN = config('TOKEN')

#Dados da previsão do tempo
def get_datas():
  data = requests.get('http://api.openweathermap.org/data/2.5/weather?id=6317872&units=metric&APPID=1d17c31f2f529e7c10426c22f5af5a6f')
  # Parse JSON into an object with attributes corresponding to dict keys.
  return json.loads(data.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

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
        'Espero que goste do nosso site:\n https://devopspbs.org/')

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

#Função de tramento de comando
def now(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Menda uma mensagem com data e hora;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    update.message.reply_text(
        datetime.datetime.now().strftime('Agora são %H:%S, %d %b %Y'))

#Função de tramento de comando
def climatempo(update, context):
    #Implemente aqui a função que vai tratar o handler/commando.
    #Menda uma mensagem de hello;
    #update: objeto que representa o retorno da API;
    #message: representa a parte do retorno referente a mensagem enviada, 
    #com dados da mensagem e metodos para manipular a mensagem;
    x = get_datas()
    update.message.reply_text(
        """
        Previsão do Tempo para Hoje em Parauapebas:
        Velocidade do Vento: {} m/s
        Pressão Atmosferica: {} hpa
        Umidade Relativa do Ar: {}%
        Temperatura Minima: {}
        Temperatura Máxima: {}
        Nascer do Sol: {}
        Por do Sol: {}
        """.format(
          x.wind.speed,
          x.main.pressure,
          x.main.humidity,
          x.main.temp_min,
          x.main.temp_max,
          x.sys.sunrise,
          x.sys.sunset          
        )        
        )

updater = Updater(TOKEN, use_context=True)

#Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('getid', get_id))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('site', site))
updater.dispatcher.add_handler(CommandHandler('links', links))
updater.dispatcher.add_handler(CommandHandler('now', now))
updater.dispatcher.add_handler(CommandHandler('climatempo', climatempo))

updater.start_polling()
updater.idle()