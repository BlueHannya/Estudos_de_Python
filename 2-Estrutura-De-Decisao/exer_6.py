""" Faça um Programa que leia três números e mostre o maior deles. """

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Para determinar o maior número podemor Usar a função max() para encontrar o maior entre os números.
maior = max(num1, num2, num3)

print(f"O maior número é: {GREEN}{maior:.2f}{WHITE}")

# Ou poderiamos fazer uma estrutura de IF, ELSE, mas vale o aprendizado dessa função.