"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário
no referido mês."""

valor = float(input("Quanto você ganha por horas?\n"))
horas = float(input("Quantas horas você trabalha por mês?\n"))

total = valor * horas

print(f"Ao final do mês você receberá R$: {total:.2f}\n")