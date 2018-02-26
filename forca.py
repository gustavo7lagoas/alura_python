

def jogar():

    print('*****************************************************')
    print('************ Bem Vindo ao Jogo da Forca *************')
    print('*****************************************************')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    
    erros = 0

    print(letras_acertadas)
    
    while(True):
        chute = input('Informe uma letra: ')
        chute = chute.strip().upper()
        
        print('Voce escolheu a letra: {}'.format(chute))

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(letra.upper() == chute.upper()):
                    letras_acertadas[posicao] = chute
                posicao += 1
        else:
            erros += 1
            print('Voce errou. Tentativa {} de 6'.format(erros + 1))

        print(letras_acertadas)

        if(erros == 6):
            print('Voce perdeu!')
            break
        if('_' not in letras_acertadas):
            print('Voce ganhou!')
            break

    print('************ Fim do Jogo *************')

if(__name__ == '__main__'):
    jogar()

