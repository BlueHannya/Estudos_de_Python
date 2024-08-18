"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

WHITE = "\033[m"
RED =  "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
TEAL = "\033[36m"
GRAY = "\033[37m"

numero_a = float(input("insira o 1 número aqui: "))

if numero_a > 0:
    print(f"Seu número '{GREEN}{numero_a:.2f}{WHITE}' é {GREEN}positivo{WHITE}")
else:
    print(f"Seu número '{RED}{numero_a:.2f}{WHITE}' é {RED}negativo{WHITE}")