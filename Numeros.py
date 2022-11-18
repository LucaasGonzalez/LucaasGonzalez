soma = 0

quantidade = 0

while True:
    
    numero = int(input("Digite um número inteiro:"))
    
    if numero == 0:
        
        break
    
    soma = soma + numero
    
    quantidade = quantidade + 1
    
print("Quantidade de números digitados:", quantidade)

print("Soma: ", soma)

print(f"Média:{soma/quantidade:10.2f}")
