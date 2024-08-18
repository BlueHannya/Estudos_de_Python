""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes
fórmulas: Para homens: (72.7*h) - 58
          Para mulheres: (62.1*h) - 44.7"""

genero = int(input("""Você se identifica como genero masculino ou feminino? Pressione
                   1 (para homem), ou 2 (para mulher)."""))
altura = float(input("\nInforme sua altura: "))
peso = float(input("\nInforme seu peso: "))

p_i = (72.7*altura) - 58 if genero == 1 else (62.1*altura) - 44.7

"""if genero == 1:
    p_i = (72.7*altura) - 58
else:
    p_i = (62.1*altura) - 44.7"""

if peso < p_i:
    print(f"\nVocê está abaixo do peso ideal, ele seria {p_i:.2f}\n")

elif peso == p_i:
    print(f"\nVocê está no peso ideal, ele seria {p_i:.2f}\n")

else:
    print(f"\nVocê está acima do peso ideal, ele seria {p_i:.2f}\n")
