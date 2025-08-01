print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************", end="\n"*2)

numero_secreto = 50
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("rodada {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        rodada=4
    else:
        if(maior):
            print("Você errou! Chute maior que o número secreto.")
        elif(menor):
            print("Você errou! Chute menor que o número secreto.")

    rodada += 1

print("Fim do jogo!")