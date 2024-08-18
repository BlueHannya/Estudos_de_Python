"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

nota_1 = float(input("Coloque sua 1 nota aqui: "))
nota_2 = float(input("Coloque sua 2 nota aqui: "))

soma = nota_1 + nota_2
media = soma / 2

if media == 10:
    print(f"Você foi {GREEN}Aprovado com distinção{WHITE}")
elif media >= 7:
    print(f"Você foi {BLUE}Aprovado{WHITE}")
else:
    print(f"Você foi {RED}Reprovado...{WHITE}")