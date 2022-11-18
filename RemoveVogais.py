// Programa em Python:
// Função para remover as vogais de uma frase.
// Se te ajudei com o código, me siga no instagram @xluucas.

def removeVogais(palavra):
    vogais = "aeiouAEIOU"

    palavraSemVogais = ""
    for cadaLetra in palavra:
        if cadaLetra not in vogais:
            
            palavraSemVogais = palavraSemVogais + cadaLetra

    return palavraSemVogais


print(removeVogais("computador"))
print(removeVogais("AnossaAulaeMuitoInteressante"))
