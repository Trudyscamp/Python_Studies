#Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um #aluno. A 
#seguir, calcule a média ponderada do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem #peso 7.5 
#(A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma #casa decimal.

A = float(input('Insira a primeira nota do aluno: '))
B = float(input('Insira a segunda nota do aluno:  '))

media = ((A*3.5)+(B*7.5))/(3.5+7.5)

print('Média = ' , format(media , '.5f'))