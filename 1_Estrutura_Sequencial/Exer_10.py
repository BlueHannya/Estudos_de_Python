"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

celsius = float(input("Informe a temperatura em Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print(f"\nSua temperatura em fahrenheit será de: {fahrenheit:.2f}")