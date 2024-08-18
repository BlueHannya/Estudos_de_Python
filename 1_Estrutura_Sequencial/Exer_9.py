"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

fahrenheit = float(input("Coloque a temperatura em fahrenheits para converte-la:\n"))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"\nSua temperatura em Celsius é de: {celsius:.2f}°.")
