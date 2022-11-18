// Programa em Python:
// Programa que procura determinado número em uma lista.
// Se te ajudei com o código, me siga no instagram @xluucas.

lista = [12, 13, 7, 9, 27, 34]

n = int(input("Digite o número a procurar: "))

x = 0

while x < len (lista):

    if lista [x] == n:

        break

    x += 1 

if x < len (lista):

        print (f"{n} - Está na posição - {x}")

else:

        print (f"{n} - Não encontrado")
        
    
