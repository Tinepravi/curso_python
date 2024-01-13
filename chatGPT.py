'''
instalar bibliotecas da Open Ia no terminal 
-> pip install openia
chave -> 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
'''

import os
import openai
#from pydantic_core import ArgsKwargs 
openai.api_key = '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'
sair = ''

while sair != 's' or sair != 'S':
    #  DEFINE COMANDOS
    pergunta_usuario = input('Digite sua pergunta: ')

    message = {'role': 'user', 'content': pergunta_usuario}

    messages = []
    messages.append(message)

    #  executando a api
    #  response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
    response = openai.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    #  lista_mens = openai.chat.completions.create(*ArgsKwargs)

    #  imprimindo a resposta
    #  print(response.choices[0].message.content)
    print(response.choices[0].message.content)

    #  print(len(response.choices))

    #  saindo do programa
    sair = input('\nDigite "s", para sair ou qualquer outra coisa pra continuar:')
    if sair == 's' or sair == 'S':
        os.system('cls')
        break
    os.system('cls')
