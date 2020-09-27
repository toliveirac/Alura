import random

def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de advinhação!")
    print("*******************************")

    pontuacao = 1000
    numero_secreto = random.randrange(1,101)

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2)Médio (3)Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for index in range(1,tentativas+1):
        print("Tentativa {} de {} ".format(index, tentativas))
        numero_recebido = input("Digite um numero entre 1 e 100: ")

        if (int(numero_recebido) < 1 or int(numero_recebido) > 100):
            print("Você deve digitar um valor entre 1 e 100")
            continue

        acertou = int(numero_recebido) == numero_secreto
        errouMaior = int(numero_recebido) > numero_secreto
        errouMenor = int(numero_recebido) < numero_secreto

        if (acertou):
            print("Você acertou, sua pontuação é: {} ! ".format(pontuacao))
            print("Fim do jogo!")
            break
        else:
            if(errouMaior):
                print("Você errou O seu chute foi maior do que o numero secreto")

            elif(errouMenor):
                print("Você errou O seu chute foi menor do que o numero secreto")

            pontuacao = pontuacao - abs(int(numero_secreto) - int(numero_recebido))

if (__name__ == "__Main__"):
    jogar()