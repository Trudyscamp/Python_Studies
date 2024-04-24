x = int(input('Insira um numero '))
y = int(input('Insira um numero '))
for i in range(1,y+1,x):
    acum = ""
    for j in range(i,i+x):
        acum = acum + str(j + ' ')
    print(acum)    