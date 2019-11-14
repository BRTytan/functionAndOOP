# faça um programa que receba dois numeros e mostre:
# a soma
# a subtração
# a multiplicação
# e a divisão entre os dois

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
soma = int(n1+n2)
subtracao = int(n1-n2)
multiplicação = int(n1*n2)
divisão = float(n1/n2)

print(f"A soma entre {n1} e {n2} = {soma}")
print(f"A subtração entre {n1} e {n2} = {subtracao}")
print(f"A multiplicação entre {n1} e {n2} = {multiplicação}")
if divisão:
    n1=float(n1)
    n2=float(n2)
    print(f"A divisão entre {n1} e {n2} = {divisão}")