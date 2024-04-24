n = int(input('Informe um numero: '))
final =0
for i in range(1,n+1):
    if str(final).find('4') == -1 and str(n).find('13') == -1:
    print(n)
    else: 
        aux = 0
        while str(n).find('4') != -1 or str(n).find('13') != -1:
            aux = aux+ 1
        final = final+aux    
print(final)        