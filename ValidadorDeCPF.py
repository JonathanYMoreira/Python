
while True:
    cpf = input('Digite um CPF, somente números: ')
    novo_cpf = cpf[:9]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)  # formula para confirmar ultimos 2 digitos do cpf
# se o resto for menor que 2 então digito 0, se for maior ou igual a 2 então é subtraido por 11 (11 - resultado)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('CPF Válido!!')
    else:
        print('CPF Inválido!!')
