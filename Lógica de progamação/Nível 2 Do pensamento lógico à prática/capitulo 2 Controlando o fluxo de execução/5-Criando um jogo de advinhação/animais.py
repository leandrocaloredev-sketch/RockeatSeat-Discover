perguntas = [ [ 'Seu animal gosta de banananas', 'macaco' ], [ 'é laranja?', 'tigre' ]]

while True:
    print('pense em uma animal...')

    acertou = False
    for pergunta in perguntas:
        resposta = input (f'{pergunta[0]} (s/n)')
        if resposta.lower() == 's':
            print (f'Você pensou em {pergunta[1]}!')
            acertou = True
            break
        
    if not acertou:
        animal= input ('Desisto! Em qual animal voce pensou? ')
        novapergunta = input ('qual pergunta você faria para diferenciar esse animal? ')
        perguntas.append([ novapergunta, animal ])
        print('perguntas')

    resposta = input('Quer jogar novamente? (s/n)')
    if resposta.lower() != 's':
       print('Obrigado por jogar!')
       break