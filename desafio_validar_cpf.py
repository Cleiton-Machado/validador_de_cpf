while True:
    def calc(num):  # função interna usada dentro da função digito()
        a = 11 - (num % 11)
        if a > 9:
            a = 0
        return a


    def digito(lista_de_numeros_cpf):  # Retorna o dígito do CPF, retorna o 1º se a lista inserida possui 9 dígitos
        # e retorna o 2º se a lista possuir 10 dígitos.
        soma_1 = 0
        for i, v in enumerate(lista_de_numeros_cpf[(len(lista_de_numeros_cpf)) - 1::-1], 2):
            mult = i * v
            soma_1 += mult
        digito = calc(soma_1)
        return digito


    cpf = input('Digite um CPF: ')
    lista = []
    for i in cpf:
        if i != '.' and i != '-' and not i.isalpha():
            lista.append(int(i))
    checagem = lista[:]
    lista = lista[0:9]
    lista.append(digito(lista))
    lista.append(digito(lista))
    sequencia = [int(cpf[0])]
    for item in range(0, 10):
        sequencia.append(int(cpf[0]))

    if lista == checagem and lista != sequencia:
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO')
