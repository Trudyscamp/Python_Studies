valor = float(input('Informe um valor: '))
qtd_100 = valor // 100
qtd_50 = valor % 100 // 50
qtd_20 = valor %100%50 //20
qtd_10 = valor %100%50%20//10
qtd_5 = valor %100%50%20%10//5
qtd_2 = valor %100%50%20%10%5//2
qtd_1 = valor %100%50%20%10%5%2

print('menor quantidade de notas:', qtd_100+qtd_50+qtd_20+qtd_10+qtd_5+qtd_2+qtd_1)
print('Notas de 100: ',qtd_100)
print('Notas de 50: ',qtd_50)
print('Notas de 20: ',qtd_20)
print('Notas de 10: ',qtd_10)
print('Notas de 5: ',qtd_5)
print('Notas de 2: ',qtd_2)
print('Notas de 2: ',qtd_2)
print('Notas de 1: ',qtd_1)