// Programa em Python:
// Programa que mostra todos os números impares de 1 ao número digitado pelo usúario.
// Se te ajudei com o código, me siga no instagram @xluucas.

x1 = int(input("Digite um número e exibirei os numeros impares de 1 até ele: "))

def impares(x1,x2,x3):
    
    cont = x1
    
    while cont <= x2:
        
        if 1 == cont % 2:
            
            print(f"{cont}")
            
            cont += x3
        else:

            cont += x3

impares(1,x1,1)
