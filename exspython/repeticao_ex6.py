#Uma pesquisa sobre algumas características físicas da população de uma determinada região
#coletou os seguintes dados referentes a cada habitante para serem analisados:
#• Sexo (“M” - Masculino, “F” - Feminino)
#• Cor dos Olhos (“A”-Azul,”V”-Verde, “C’-Castanho)
#• Idade em anos
#Para cada habitante foi digitada uma linha com esses dados e a última linha, que não corresponde a 
#ninguém conterá o valor de idade igual a -1. Fazer um programa que determine e imprima:
#a) A maior idade dos habitantes;
#b) A porcentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e
#que tenham olhos verdes

idade = 0
sexo = ''
olhos = ''
maioridade = 0
mulheres = 0
total = 0
while idade <= 35:
    if idade == -1: break
    sexo = input('informe o sexo M ou F: ')
    olhos = input('informe a cor dos olhos A para azul, V para verde e C para castanho: ')
    idade = int(input('informe a idade: '))
    total+=1 #total de pessoas
    if idade > maioridade: #calcula a maior idade
        maioridade = idade
    
    
    if idade >=18 and idade <36 and olhos == 'V' and sexo == 'F': #conta individuos do sexo feminino com 18 a 35 de olhos verdes
        mulheres+=1
        
            
print(maioridade)
print((mulheres/total)*100)    