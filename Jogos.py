import Forca
import Adivinhacao2

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************", end="\n" * 2)

print("1- Forca 2- Adivinhação")
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Abrindo jogo da Forca...")
    Forca.jogar()
elif(jogo == 2):
    print("Abrindo jogo de Adivinhação...")
    Adivinhacao2.jogar()
