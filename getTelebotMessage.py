import telepot
import time

bot = telepot.Bot("412555656:AAFCMbE1G8GiAy45fwK5BFdCrmjQbut8DOI")

def escutaMesagens(menssagem):
	msg = menssagem['text']

	if msg == "ola":
		time.sleep(2)
		bot.sendMessage(menssagem['chat']['id'], 'olá, tudo bem?')

	if msg == "arduino":
		bot.sendMessage(menssagem['chat']['id'], "http://escoladoarduino.com.br/curso/")

bot.message_loop(escutaMesagens)

while True:
	pass