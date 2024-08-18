""" Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
-Imposto de Renda-, que depende do salário bruto (conforme tabela abaixo) e 3% para o -Sindicato- e
que o -FGTS- corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5
e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

lucro_hora = float(input("Qual o valor que você ganha por horas trabalhadas: "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês: "))
salario_bruto = lucro_hora * horas_trabalhadas

if salario_bruto <= 900:

    ir = salario_bruto * 0.00
    inss = salario_bruto * 0.10
    fgts  = salario_bruto * 0.11
    sindicato = salario_bruto * 0.03
    imposto_total = salario_bruto * 0.24
    salario_liquido = salario_bruto - imposto_total

    print(f"""\nSeu salário bruto será de R$:{GREEN}{salario_bruto:.2f}{WHITE}
Seu desconto no IR referente ao seu salário bruto será de R$:{RED}{ir:.2f}{WHITE}
Seu desconto no INSS referente ao seu salário bruto será de R$:{RED}{inss:.2f}{WHITE}
Seu desconto no Sindicato referente ao seu salário bruto será de R$:{RED}{sindicato:.2f}{WHITE}
Seu desconto total em Imposto referente ao seu salário bruto será de R$:{RED}{imposto_total:.2f}{WHITE}
Seu salário liquido será de R$:{TEAL}{salario_liquido:.2f}{WHITE}\n""")

elif salario_bruto >= 901 and salario_bruto <=1500:

    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.10
    fgts  = salario_bruto * 0.11
    sindicato = salario_bruto * 0.03
    imposto_total = salario_bruto * 0.29
    salario_liquido = salario_bruto - imposto_total

    print(f"""\nSeu salário bruto será de R$:{GREEN}{salario_bruto:.2f}{WHITE}
Seu desconto no IR referente ao seu salário bruto será de R$:{RED}{ir:.2f}{WHITE}
Seu desconto no INSS referente ao seu salário bruto será de R$:{RED}{inss:.2f}{WHITE}
Seu desconto no Sindicato referente ao seu salário bruto será de R$:{RED}{sindicato:.2f}{WHITE}
Seu desconto total em Imposto referente ao seu salário bruto será de R$:{RED}{imposto_total:.2f}{WHITE}
Seu salário liquido será de R$:{TEAL}{salario_liquido:.2f}{WHITE}\n""")

elif salario_bruto >= 1501 and salario_bruto <=2500:

    ir = salario_bruto * 0.10
    inss = salario_bruto * 0.10
    fgts  = salario_bruto * 0.11
    sindicato = salario_bruto * 0.03
    imposto_total = salario_bruto * 0.34
    salario_liquido = salario_bruto - imposto_total

    print(f"""\nSeu salário bruto será de R$:{GREEN}{salario_bruto:.2f}{WHITE}
Seu desconto no IR referente ao seu salário bruto será de R$:{RED}{ir:.2f}{WHITE}
Seu desconto no INSS referente ao seu salário bruto será de R$:{RED}{inss:.2f}{WHITE}
Seu desconto no Sindicato referente ao seu salário bruto será de R$:{RED}{sindicato:.2f}{WHITE}
Seu desconto total em Imposto referente ao seu salário bruto será de R$:{RED}{imposto_total:.2f}{WHITE}
Seu salário liquido será de R$:{TEAL}{salario_liquido:.2f}{WHITE}\n""")

else:

    ir = salario_bruto * 0.20
    inss = salario_bruto * 0.10
    fgts  = salario_bruto * 0.11
    sindicato = salario_bruto * 0.03
    imposto_total = salario_bruto * 0.44
    salario_liquido = salario_bruto - imposto_total

    print(f"""\nSeu salário bruto será de R$:{GREEN}{salario_bruto:.2f}{WHITE}
Seu desconto no IR referente ao seu salário bruto será de R$:{RED}{ir:.2f}{WHITE}
Seu desconto no INSS referente ao seu salário bruto será de R${RED}{inss:.2f}{WHITE}
Seu desconto no Sindicato referente ao seu salário bruto será de R$:{RED}{sindicato:.2f}{WHITE}
Seu desconto total em Imposto referente ao seu salário bruto será de R$:{RED}{imposto_total:.2f}{WHITE}
Seu salário liquido será de R$:{TEAL}{salario_liquido:.2f}{WHITE}\n""")
