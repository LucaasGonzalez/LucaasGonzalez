// Programa em Python:
// Programa que calcula o Fatorial de um valor digitado.
// Se te ajudei com o código, me siga no instagram @xluucas.

resposta = 'sim'
 
while ( resposta == 'sim' or resposta == 's' ):

    x = int (input("Digite seu número para calcular o fatorial: "))

    fatorial = contador = 1
    
    while (contador <= x):
    
        fatorial = fatorial * contador
        contador = contador + 1

    print ("O fatorial é: ", fatorial)
    resposta = input ("Deseja continuar? ")
                                                                                                                                                  
    resposta = resposta.lower()
        

        


    
