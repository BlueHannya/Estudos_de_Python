"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos 
dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$"""

lucro_hora = float(input("Qual o valor que você ganha por horas trabalhadas: "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês: "))
salario_bruto = lucro_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
imposto_total = salario_bruto * 0.25
salario_liquido = salario_bruto - imposto_total

print(f"\nSeu salário bruto será de R$:{salario_bruto:.2f}\n")

print(f"\nSeu desconto no IR referente ao seu salário bruto será de R$:{ir:.2f}\n")

print(f"\nSeu desconto no INSS referente ao seu salário bruto será de R$:{inss:.2f}\n")

print(f"\nSeu desconto no Sindicato referente ao seu salário bruto será de R$:{sindicato:.2f}\n")

print(f"\nSeu desconto total em Imposto referente ao seu salário bruto será de R$:{imposto_total:.2f}\n")

print(f"\nSeu salário liquido será de R$:{salario_liquido:.2f}\n")
