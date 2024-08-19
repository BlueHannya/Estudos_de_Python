"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

num1 = float(input("\nInforme sua nota do 1 bimestre para calculár-mos sua média: "))
num2 = float(input("\nInforme sua nota do 2 bimestre para calculár-mos sua média: "))
num3 = float(input("\nInforme sua nota do 3 bimestre para calculár-mos sua média: "))
num4 = float(input("\nInforme sua nota do 4 bimestre para calculár-mos sua média: "))

soma = num1 + num2 + num3 + num4
media = float(soma/4)

print(f"""\nSuas notas desse ano foram de:\n\n- No primeiro bimestre {num1:.2f}\n- No segundo bimestre {num2:.2f}
- No terceiro bimestre {num3:.2f}\n- No quarto bimestre {num4:.2f}\n\nSua média anual é de: {media:.2f}""")

if media >= 5:
    print("\nAluno Aprovado!!!\n")
else:
    print("\nAluno Reprovado...\n")
