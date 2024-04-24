nome = input('Insira o nome completo:')
cpf = input('Informe o CPF: ')
primeironome = nome[:nome.find(' ')]
ultimonome = nome[::-1][:nome.find(' ')][::-1]

usuario = primeironome.lower() + '.' + ultimonome.lower()

senha = cpf[-2:] + '@' + ultimonome[0].upper()
print(usuario, senha)
