"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

num1 = float(input("Informe sua nota do 1 bimestre para calculár-mos sua média: "))
num2 = float(input("Informe sua nota do 2 bimestre para calculár-mos sua média: "))
num3 = float(input("Informe sua nota do 3 bimestre para calculár-mos sua média: "))
num4 = float(input("Informe sua nota do 4 bimestre para calculár-mos sua média: "))

soma = num1 + num2 + num3 + num4
media = float(soma/4)

print(f"Suas notas desse ano foram de:\nNo primeiro bimestre {num1:.2f},\nNo segundo bimestre {num2:.2f},\nNo terceiro bimestre {num3:.2f},\nNo quarto bimestre {num4:.2f}.\nSua média anual é de: {media:.2f}")

if media >= 5:
    print("\nAluno Aprovado!!!")
else:
    print("\nAluno Reprovado...")