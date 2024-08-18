""" Faça um programa que calcule as raízes de uma equação do segundo grau, na forma 
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;

- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
usuário e encerre o programa;

- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
informe-a ao usuário;

- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao 
usuário; """

import math

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

a = float(input("\n- Informe o valor de 'A': "))

if a == 0:
    print("\nDesculpa, isso {RED}não é{WHITE} uma equação de segundo grau\n")
else:
    b = float(input("\n- Informe o valor de 'B': "))
    c = float(input("\n- Informe o valor de 'C': "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print(f"\nA equação {RED}não possui{WHITE} raizes reais.\n")

    elif delta == 0:
        equacao= -b / 2 * a
        print(f"\nA esquação {BLUE}possui apenas uma raiz real{WHITE}, que é: {equacao}.\n")

    else:
        equacao1 = (-b + math.sqrt(delta)) / (2 * a)
        equacao2 = (-b - math.sqrt(delta)) / (2 * a)
        resultado = f"{equacao1:.2f} e {equacao2:.2f}"
        print(f"\nA esquação {GREEN}possui duas raizes reais{WHITE}, que são: {resultado}.\n")

# 