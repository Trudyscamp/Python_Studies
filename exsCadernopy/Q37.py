soma =0
for i in range(2):
    nome = input('Informe seu nome: ')
    opcao = input('Informe sua opção: ')
    numero = int(input('Informe seu número'))
    if opcao == 'par':
        nome_par = nome
    else:
        nome_impar = nome
    soma= soma + numero          
if soma %2 == 0 :
    print(nome_par)
else:
    print(nome_impar)        