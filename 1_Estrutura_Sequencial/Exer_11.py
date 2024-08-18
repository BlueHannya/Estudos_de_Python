"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

n1 = int(input("Coloque um número inteiro aqui:"))
n2 = int(input("Coloque outro número inteiro aqui:"))
n3 = float(input("Coloque um número real aqui:"))

resultado1 = (n1 ** 2) + (n2 / 2)
resultado2 = (n1 * 3) + n3
resultado3 = (n3 ** 3)

print(f"\nO produto do dobro do primeiro com metade do segundo é: {resultado1:.2f}")

print(f"\nA soma do triplo do primeiro com o terceiro é: {resultado2:.2f}")

print(f"\nO terceiro número elevado ao cubo é: {resultado3:.2f}\n")