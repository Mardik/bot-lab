FROM python
RUN mkdir /bot
WORKDIR /bot
RUN pip install python-telegram-bot
RUN pip install python-decouple
