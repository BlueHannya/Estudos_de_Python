""" Faça um Programa que leia três números e mostre-os em ordem decrescente. """

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

# Há duas funções ao qual podemos ordenar uma lista, vamos ver o primeiro '.sort()'

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse = True)

# Nela alteramos a própria lista, assim mudando sua ordem, no caso 'sort(reverse=true)' fazemos a de forma decrescente

print(f"\nOs números na ordem {YELLOW}decrescente{WHITE} ficam: {YELLOW}{numeros}{WHITE}\n")