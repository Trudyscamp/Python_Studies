l1 = float(input('Informe o lado 1: '))
l2 = float(input('Informe o lado 2: '))
l3 = float(input('Informe o lado 3: '))

if (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2):
    if l1 == l2 and l2==l3:
        print('Triângulo equilátero')
    elif l1 != l2 and l1!=l3 and l2!=l3:
        print('Triângulo escaleno')
    else:
        print('Triângulo isóceles')     
        
        
else:
    print('Não é um triângulo')    