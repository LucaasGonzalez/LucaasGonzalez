// Programa em Python:
// Programa que conta quantas letras determinadas tem em uma frase.
// Se te ajudei com o código, me siga no instagram @xluucas.

def conta(texto, letra):
    contadorLetra = 0
    
    for c in texto:
        if c == letra:
            contadorLetra = contadorLetra + 1
    return contadorLetra

def main():

    frase = input ("Digite uma frase: ")
    caracter = input ("Digite a letra que deseja procurar: ")
    print(conta(frase, caracter))
