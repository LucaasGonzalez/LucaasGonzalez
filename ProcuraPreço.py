// Programa em Python:
// Programa que procura o preço de um produto através da sua categoria.
// Se te ajudei com o código, me siga no instagram @xluucas.

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preço = 10

elif categoria == 2:
    preço = 18

elif categoria == 3:
    preço = 23

elif categoria == 4:
    preço = 26

elif categoria == 5:
    preço = 31

if categoria >= 6:

     print("Categoria inválida, digite um valor entre 1 e 5!")

else:

    print(f"o preço do produto é: R$ {preço:6.2f}")
