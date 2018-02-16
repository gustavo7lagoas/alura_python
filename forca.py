

def jogar():

    print('*****************************************************')
    print('************ Bem Vindo ao Jogo da Forca *************')
    print('*****************************************************')

    palavra_secreta = 'banana'
    
    acertou = False
    enforcou = False
    
    while(not acertou and not enforcou):
        chute = input('Informe uma letra: ')
        chute = chute.strip()
        
        print('Voce escolheu a letra: {}'.format(chute))

        posicao = 0

        for letra in palavra_secreta:
            if(letra.upper() == chute.upper()):
                print('A letra {} aparece na posicao {}'.format(letra, str(posicao + 1)))
            posicao += 1

    print('************ Fim do Jogo *************')

if(__name__ == '__main__'):
    jogar()

