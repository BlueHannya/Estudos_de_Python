"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

periodo = input("\nDigite M-matutino ou V-Vespertino ou N- Noturno para mostrar seu periodo do dia: ")

if periodo == "M" or periodo == "m":
    print("\nTenha um Bom Dia!\n")
elif periodo == "V" or periodo == "v":
    print("\nTenha uma Boa Tarde!\n")
elif periodo == "N" or periodo == "n":
    print("\nTenha uma Boa Noite!\n")
else:
    print(f"\nValor {RED}Inválido!{WHITE}\n")