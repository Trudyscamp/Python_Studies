#Faça um programa que leia 20 números inteiros e apresente:
#a. Média dos ímpares
#b. Maior número par
#c. Diferença do maior menos o menor número

soma = 0 #inicializando o contador da soma
maiorvalorpar = 0 #inicializando o contador do maiorvalor par
maiornumero = 0 #inicializando o contador do maior numero
menornumero = 99999999999999999 #inicializando o contador do menor numero
for i in range(20): #estabelendo a condição de repetição
    numero = int(input('Digite um número: ')) #Recebendo um número inteiro           
    
    if numero > maiornumero: #estabelecendo a condição para achar o maior numero
        maiornumero = numero #atribui o maior numero a variavel
    else:
        menornumero = numero #atribui o menor valor a variavel
    
    if numero%2 ==1: #condição caso seja impar
        soma = soma+numero #soma dos numeros
    elif numero%2 == 0: #condição caso seja par
        if maiorvalorpar < numero: #confição para o maior valor par
            maiorvalorpar = numero #atribuição do maior valor a variavel
            
print('A média é igual a: ' , format(soma/20 , '.2f')) #imprime a média a dividindo por 3 e formata para 2 casas decimais apos a virgula
print('O maior valor par é: ' , maiorvalorpar) #imprime o maior valor
print('A diferença entre o maior valor e o menor valor é: ' , maiornumero - menornumero) #a diferença do maior valor com o menor valor