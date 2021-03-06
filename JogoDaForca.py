#secreto = 'suspresa'
digitadas = []
chances = 3
baixar_tela = 'Vamos Começar'
registro = []

def linha():
    print('--------------------------------------------------------------------------')

print('Vamos jogar forca!')
secreto = input('Digite uma palavra? ')
secreto = secreto.lower()
dica = input('Digite uma dica? ')

# usado para dar um espaço e não mostrar senha na tela
for aux in baixar_tela:
    print(aux)

while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    print(f'A dica é : {dica}')
    letra = input('Digite uma letra: ')
    letra = letra.lower()

    if len(letra) > 1:
        print('Isso não esta certo, digite apenas uma letra! ')
        continue
    registro += letra  # usado para salvar letras para usar de consulta
    digitadas.append(letra)  # acrescenta o digito ao final da variavel letra
    digitadas.append(registro)

    if letra in secreto:
        print('')
        print(f'a letra {letra} existe na palavra secreta')
        print(f'Você ainda tem {chances} tentativas!')
        print(f'A dica é : {dica}')
        print(f'Regitro de letras: {registro}')
        print('')
    else:
        print('')
        print(f'Não temos a letra {letra} tente novamente: ')
        print(f'Você ainda tem {chances} tentativas!')
        print(f'A dica é : {dica}')
        print(f'Regitro de letras: {registro}')
        print('')
        digitadas.pop()  # remove a variavel digitado, pois não esta na palavra secreta

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        elif secreto_temporario == ' ':
            secreto_temporario += '_'
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        linha()
        print('Você acertou a palavra toda!!')
        linha()
        break
    else:
        print(f'A palavra esta assim {secreto_temporario}')

    if letra not in secreto:
        chances += -1
