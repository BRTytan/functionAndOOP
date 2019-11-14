# faça um programa que receba quatro numero e mostre a media entre os quatrp
# dica media = (n1+n2+n3+n4)/4
# Usar input

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))
resultado = (n1+n2+n3+n4)/4
print(f"suas notas são: {n1},{n2},{n3},{n4} e sua media é: {resultado}")

if resultado >= 6.0:
    print("Você passou")
else:
    print("Você foi reprovado")