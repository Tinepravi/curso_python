letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'sair' in letras:
        print('Saindo...')
        break

    print(letras)