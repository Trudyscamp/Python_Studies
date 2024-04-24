maior_idade = 0 
while True:
    idade = int(input('Insira a idade: '))
    if idade == 100: break
    if idade > maior_idade:
        maior_idade = idade
        
print(maior_idade)        