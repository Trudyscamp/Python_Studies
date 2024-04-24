#Faça um programa que leia o nome e a idade de 15 pessoas e apresente:
#a. Maior idade
#b. Nome da pessoa mais nova
#c. Média das idades
soma = 0 #inicializando o contador da soma
maioridade = 0 # inicializando o contador da maioridade
menor = '' #inicialiando o acumulador da menoridade
menoridade = 200000000
for i in range(15):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    soma = soma + idade
    
    if idade > maioridade:
        maioridade = idade
    
    if idade < menoridade:
        menoridade = idade
        menor = nome    
    
print('A maior idade é: ', maioridade)
print('O nome da pessoa de menor idade é:' , menor)
print('A média das idades é de: ' , format(soma/15 , '.2f'))        