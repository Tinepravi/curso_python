'''
validadndo cpf
'''
import re
import sys
import random


#cpf = '010.595.154-40'.replace('.', '').replace('-', '') # remove pontos e traços
#nove_digitos = cpf[:9]

#gerando cpf
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

#entrada = input('Digite um CPF: ')
entrada = nove_digitos
cpf = re.sub(
    r'[^0-9]', 
    '',
    entrada
    )
nove_digitos = cpf[:9]

sequencia = entrada == entrada[0] * len(entrada)
#primeiro_caractere = entrada[0]
#primeiro_caractere_repetido = primeiro_caractere * len(entrada)

if sequencia:
    print('Caracteres repetidos!')
    print('Finalizando programa!')
    sys.exit()

#print(nove_digitos)
contador_regressivo_1 = 10

resultado_digito_1 = 0
#validando primeiro dito
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

#print(digito_1)


#validando segundo digito
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

#print(digito_2)
#print(digito_1, digito_2, sep='')

#validando cpf
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
cpf = f'{cpf}{digito_1}{digito_2}'


if cpf == novo_cpf:
    print(f"{cpf} é válido!")
else:
    print(f'{cpf} é inválido!')