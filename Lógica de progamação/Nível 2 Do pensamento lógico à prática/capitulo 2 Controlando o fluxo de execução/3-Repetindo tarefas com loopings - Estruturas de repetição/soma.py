soma = 0

n = 1

#while n <= 10:
#    soma = soma + n
#    n = n + 1 

for index in range(1,11):  # range é um intervalo, e o index é o número
    soma  += index

    #soma = som([i for i in range(1,11)])

print (f'A soma dos números de 1 a 10 é: {soma}')  # print(f'soma: {soma}')
    