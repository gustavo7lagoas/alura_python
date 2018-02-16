import random


def jogar():
    print('******************************************')
    print('**** Bem Vindo ao Jogo de Adivinhacao ****')
    print('******************************************')
    
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    
    print('Informe o nivel de dificuldade - (1) facil (2) medio (3) dificil')

    nivel = int(input('Informe o nivel de dificuldade: '))

    if(nivel == 1):
        numero_tentativas = 20
    elif(nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    for rodada in range(1, numero_tentativas + 1):
        print('Tentativa {0} de {1}'.format(rodada, numero_tentativas))
        chute = int(input('Informe um numero entre 1 e 100: '))
        
        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if(chute < 1 or chute > 100):
            print('Digite um numero entre 1 e 100')
            continue

        if(acertou):
            print('Voce acertou o numero secreto')
            print('Voce fez {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('O numero digitado e maior que o numero secreto')
            else:
                print('O numero digitado e menor que o numero secreto')
            pontos = pontos -abs(numero_secreto - chute)

    print('**** Fim do Jogo ****')

if(__name__ == '__main__'):
    jogar()
