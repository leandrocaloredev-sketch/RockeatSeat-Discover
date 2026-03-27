print('Olà, eu sou sua assistente, Pitoso. O que você deseja fazer?+')

comando = input('digite um comando:')

#match é uma estrutura de fluxo que permite comparar um valor em vários padroes diferentes, e executar um bloco de código diferente para cada padrão.
match comando:
    case 'oi':
        print('Oi, como vai você!')
    case 'tchau':
        print('Tchau, até mais!')
    case 'piada':
        print('Qual é o animal mais antigo do mundo? A zebra, porque ela é em preto e branco!')
    case 'clima':
        print('ta muuuuuuuuuuuito quente!! Deve ter passado de 35 graus hoje!')
    case _:
        print('Desculpe, não entendi o comando.')

        #case é como se fosse um if, elif, else, mas escrito de forma mais simples