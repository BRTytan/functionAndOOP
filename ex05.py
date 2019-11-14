# Escreva um programa que leia o nome de um funcionário, seu número de horas trabalhadas, o
# valor que recebe por hora e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.

nome = input("Qual seu nome: ")
horas_trabalhadas = int(input("Quantas horas trabalhadas: "))
recebe_hora = float(input("Quanto voce recebe por hora: "))
salario = horas_trabalhadas*recebe_hora
print(f"o {nome} recebe R${salario}")