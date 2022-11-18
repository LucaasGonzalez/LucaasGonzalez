// Programa em Python:
// Programa que mostra o quanto irá pagar de fatura por minutos utilizados.
// Se te ajudei com o código, me siga no instagram @xluucas.

minutos = int(input("Quantos minutos foram utilizados no mês: "))

if minutos < 200:
    preço = 0.20

else:

    if minutos < 400:
        preço = 0.18

    else:
        preço = 0.15

print(f"Você vai pagar este mês: R$ {minutos*preço:6.2f}")
    
    
