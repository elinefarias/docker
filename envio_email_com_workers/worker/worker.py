import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
  r = redis.Redis(host='queue', port=6379, db=0)
  while True:
      mensagem = json.loads(r.blpop('sender')[1])
      
      # Simulando envio de e-mail...
      print('Enviando e-mail...')
      print('Assunto: {}'.format(mensagem['assunto']))
      print('Mensagem: {}'.format(mensagem['mensagem']))
      sleep(randint(15, 45))
      print('E-mail enviado com sucesso!')
      print('-----------------------------------')