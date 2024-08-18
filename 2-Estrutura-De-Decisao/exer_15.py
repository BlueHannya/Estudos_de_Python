""" Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno. Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes; """

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

lado1 = float(input("\n- Informe o primeiro lado do triângulo: "))
lado2 = float(input("\n- Informe o segundo lado do triângulo: "))
lado3 = float(input("\n- Informe o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 ==  lado2 == lado3:
        print(f"\nVocê tem um {GREEN}Triângulo Equilatero{WHITE} aqui!!!\n")
    elif lado1 ==  lado2 or  lado1 == lado3 or lado2 == lado3:
        print(f"\nVocê tem um {PURPLE}Triângulo Isósceles{WHITE} aqui!!!\n")
    else:
        print(f"\nVocê tem um {TEAL}vTriângulo Escaleno{WHITE} aqui!!!\n")
else:
    print(f"\nIsso {RED}não é{WHITE} um triângulo.\n")
