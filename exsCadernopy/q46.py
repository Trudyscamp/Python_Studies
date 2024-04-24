n1 = int(input('Informe um numero: '))
n2 = int(input('Informe um numero: '))
f1 = 1
f2 = 1
for i in range(1,n1+1):
    f1 = f1 * i
for i in range(1,n2+1):
    f2 = f2 * i
print(f1 + f2)        
