while True:
    nome = input('informe o nome de 10 caracteres ao menos: ')
    if len(nome )>=10 : break
    print('Nome inálido.')
    
meio = len(nome) //2
p1 = nome[:meio]
p2 = nome[meio:]
    
senha=p2[:2]+'%%'+p1[-3:]
print(p1,p2,senha)