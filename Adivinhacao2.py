import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************", end="\n"*2)

    numero_secreto = random.randrange(0, 101)
    pontos = 1000

    nivel_str = input("Qual nivel de dificuldade? (1-Facil, 2-Medio e 3-Dificil) ")
    nivel = int(nivel_str)

    if (nivel == 1):
        total_tentativas = 20

    elif (nivel == 2):
        total_tentativas = 10

    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("rodada {:02d} de {:02d}".format(rodada, total_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break

        else:
            if(maior):
                print("Você errou! Chute maior que o número secreto.")
                if(rodada == total_tentativas):
                    print("O numero secreto era {} você fez {} pontos".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! Chute menor que o número secreto.")
                if (rodada == total_tentativas):
                    print("O numero secreto era {} você fez {} pontos".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()