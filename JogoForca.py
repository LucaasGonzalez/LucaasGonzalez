// Programa em Python:
// Jogo da forca em Python.
// Se te ajudei com o código, me siga no instagram @xluucas.

print("*" * 37)
print("**** Bem vindo ao jogo da forca! ****")
print("*" * 37)

palavra_secreta = "banana"

letras_acertadas = ['_','_','_','_','_','_']

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while (not acertou and not enforcou):
    
    chute = input ("Qual letra?")
    
    if (chute in palavra_secreta):
        
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                #print("Encontrei a letra {} na posição {}" .format(letra, posicao))
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        
        erros += 1

    acertou = '_' not in letras_acertadas
    enforcou = erros == 6
    print (letras_acertadas)

if(acertou):
        
    print ('\n Você Ganhou!!! \n')
        
else:
        
    print('\n Você Perdeu :( \n')
    
    print ("Fim de Jogo, obrigado por jogar!")

