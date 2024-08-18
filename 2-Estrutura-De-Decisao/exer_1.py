"""Faça um Programa que peça dois números e imprima o maior deles."""

WHITE = "\033[m"
RED =  "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
TEAL = "\033[36m"
GRAY = "\033[37m"

numero_a = float(input("insira o 1 número aqui: "))
numero_b = float(input("Insira o 2 número aqui: "))

if numero_a > numero_b:
    print(f"\nO 1 número '{GREEN}{numero_a:.2f}{WHITE}', é maior que o 2 número '{RED}{numero_b:.2f}{WHITE}'.")
elif numero_a == numero_b:
    print(f"\nO 1 número '{GREEN}{numero_a:.2f}{WHITE}', e o 2 número '{RED}{numero_b:.2f}{WHITE}' tem o mesmo valor.")
else:
    print(f"\nO 2 número '{GREEN}{numero_b:.2f}{WHITE}', é maior que o 1 número '{RED}{numero_a:.2f}{WHITE}'.")
