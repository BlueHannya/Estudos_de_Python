""" Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. """

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

nota_1 = float(input(f"\nColoque sua 1 nota aqui: {YELLOW}"))
nota_2 = float(input(f"\n{WHITE}Coloque sua 2 nota aqui: {YELLOW}"))

soma = nota_1 + nota_2
media = soma / 2

if media >= 0 and media < 4.1:
    print(f"\n{WHITE}Você foi {RED}Reprovado...{WHITE} seu nota foi '{RED}E{WHITE}'...\n")
elif media > 4 and media < 6.1:
    print(f"\n{WHITE}Você foi {RED}Reprovado...{WHITE} seu nota foi '{RED}D{WHITE}'...\n")
elif media > 6 and media < 7.6:
    print(f"\n{WHITE}Você foi {BLUE}Aprovado{WHITE} sua nota foi '{BLUE}C{WHITE}'.\n")
elif media > 7.5 and media < 9.1:
    print(f"\n{WHITE}Você foi {BLUE}Aprovado{WHITE} sua nota foi '{BLUE}B{WHITE}'.\n")
else:
    print(f"""\n{WHITE}Você foi {GREEN}Aprovado com distinção{WHITE} sua nota
foi '{GREEN}A{WHITE}'.\n""")
