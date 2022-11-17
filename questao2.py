from random import randint
opcao = int(input("Digite um número [1] jogador x computador  [2] :"))

if opcao == 1:
    jogador1 = list()

    jogador2 = list()

    print('SIMULADOR DE JOGO DADO')

    quant = 2

    total = 1

    while total <= quant:

        cont = 0

        while True:

            num = randint(1,6)

            if num not in jogador1:

                jogador1.append(num)

                cont += 1

            if cont >=1:

                break

        jogador1.sort()

        jogador2.append(jogador1[:])

        jogador1.clear()

        total +=1



    for i, l in enumerate(jogador2):

        print(f'jogador{i+1}:{l}')


