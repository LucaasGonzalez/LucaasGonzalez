// Programa em Python:
// Exemplo de criação de funções.
// Se te ajudei com o código, me siga no instagram @xluucas.

def multiplo (a, b):
    return (a % b == 0) or (b % a == 0)


x = int ( input ("Digite um número: "))

y = int ( input ("Digite outro número: "))

print ("Os números são múltiplos?", multiplo (x, y))
