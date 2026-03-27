#inset() Insere um elemento em uma posição específica de uma lista.

#sort() Ordena os elementos de uma lista em ordem crescente.

#reverse() Inverte a ordem dos elementos de uma lista.

#append()  Adiciona um elemento ao final de uma lista.

#pop()   Remove o ultimo elemnto da lista

notas = [8,8,9,3,5]

media = 0
for nota in notas:
    media += nota

    media /=4

    print(f'A média é {media}')