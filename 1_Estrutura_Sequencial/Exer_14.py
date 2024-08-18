"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele
traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de
R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
os dados do programa com as mensagens adequadas."""

peso_peixe = float(input("Informe quantos kg você pescou de peixe: "))

regulamento = 50

"""if peso_peixe > regulamento:
    multa = (peso_peixe - regulamento) * 4
    print(f"Você ultrapassou a pessagem pré estabelecida, pague R$: {multa:.2f} de multa.")
else:
    print("Você não ultrapassou a pesagem estabelecida, pode retirar os peixes.")"""

# Calcula o excesso e a multa usando operadores ternários
excesso = peso_peixe - regulamento if peso_peixe > regulamento else 0
multa = excesso * 4

# Imprime a mensagem adequada com base no peso do peixe
print(f"Você ultrapassou a pesagem pré-estabelecida, pague R$: {multa:.2f} de multa." 
      if peso_peixe > regulamento 
      else "Você não ultrapassou a pesagem estabelecida, pode retirar os peixes.")