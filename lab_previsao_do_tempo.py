from datetime import datetime

from telegram.ext import Updater, CommandHandler
from decouple import config
from collections import namedtuple
import json
import requests

TOKEN = config('TOKEN')


# Dados da previsão do tempo vinda da API do openweathermap.
def get_datas():
    data = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id=6317872&units=metric&APPID=1d17c31f2f529e7c10426c22f5af5a6f')
    # Parse JSON into an object with attributes corresponding to dict keys.
    return json.loads(data.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


# Updater - Dados novos enviados
# CommandHandler - Instância de um comando.

# Função de tramento de comando
def clima_tempo(update, context):
    # Implemente aqui a função que vai tratar o handler/commando.
    # Menda uma mensagem de hello;
    # update: objeto que representa o retorno da API;
    # message: representa a parte do retorno referente a mensagem enviada,
    # com dados da mensagem e metodos para manipular a mensagem;
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
            datetime.fromtimestamp(x.sys.sunrise).strftime('%H:%M'),
            datetime.fromtimestamp(x.sys.sunset).strftime('%H:%M')
        )
    )


updater = Updater(TOKEN, use_context=True)

# Vincula função a handler/commando.
updater.dispatcher.add_handler(CommandHandler('clima_tempo', clima_tempo))

updater.start_polling()
updater.idle()

# Referências
# https://requests.readthedocs.io/en/master/
