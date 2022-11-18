// Programa em Python:
// Tabuada.
// Se te ajudei com o código, me siga no instagram @xluucas.

numero = int(input("Digite o numero da tabuada: \n"))

numero2= int(input ("Digite o numero do inicio da tabuada: \n"))

numero3= int(input ("Digite o numero do fim da tabuada: \n"))
    
for contador in range(numero2, numero3 + 1):

    print(numero," x ",contador," = ",numero*contador, "\n")
    
