"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

salario = float(input("Informe seu salário: "))

if salario <= 279 :

    AUMENTO = 0.20
    reajuste = salario * AUMENTO
    salario_novo = salario + reajuste
    print(f"""\nSeu salário é de {salario:.2f}
o percentual de aumento aplicado é de {GREEN}20%{WHITE}
o valor do aumento será de: {GREEN}{reajuste:.2f}{WHITE}
Seu novo salário será de: {GREEN}{salario_novo:.2f}{WHITE}\n""")

elif salario >= 280 and salario <= 699:

    AUMENTO = 0.15
    reajuste = salario * AUMENTO
    salario_novo = salario + reajuste
    print(f"""\nSeu salário é de {salario:.2f}
O percentual de aumento aplicado é de {GREEN}15%{WHITE}
O valor do aumento será de: {GREEN}{reajuste:.2f}{WHITE}
Seu novo salário será de: {GREEN}{salario_novo:.2f}{WHITE}\n""")

elif salario >= 700 and salario <= 1499:

    AUMENTO = 0.10
    reajuste = salario * AUMENTO
    salario_novo = salario + reajuste
    print(f"""\nSeu salário é de {salario:.2f}
o percentual de aumento aplicado é de {GREEN}10%{WHITE}
o valor do aumento será de: {GREEN}{reajuste:.2f}{WHITE}
Seu novo salário será de: {GREEN}{salario_novo:.2f}{WHITE}\n""")

else:

    AUMENTO = 0.05
    reajuste = salario * AUMENTO
    salario_novo = salario + reajuste
    print(f"""\nSeu salário é de {salario:.2f}
o percentual de aumento aplicado é de {GREEN}5%{WHITE}
o valor do aumento será de: {GREEN}{reajuste:.2f}{WHITE}
Seu novo salário será de: {GREEN}{salario_novo:.2f}{WHITE}\n""")
