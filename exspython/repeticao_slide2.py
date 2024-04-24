from audioop import mul


somaaltura = 0
maior_altura = 0
contamulher = 0
contahomem = 0
while True:
    if sexo == 'FIM': break
    altura = float(input('Insira a altura: '))
    sexo = input('insira o sexo: ')
    
    if altura > maior_altura:
        maior_altura = altura
    
    if sexo == 'F':
        somaaltura = somaaltura+altura
        contamulher+=1
    else:
        contahomem+=1
print(maior_altura)
print(somaaltura/conta)                
           