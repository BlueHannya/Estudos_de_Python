""" Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo,
2- Segunda, etc.), se digitar outro valor deve aparecer 'valor inválido.' """

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

dia_semana = float(input("\nDigite um número de 1 a 7 para ver qual será o dia da semana: "))

if dia_semana == 1:
    print(f"\nO dia será {PURPLE}Domingo{WHITE}!!!\n")
elif dia_semana == 2:
    print(f"\nO dia será {YELLOW}segunda-feira{WHITE}!!!\n")
elif dia_semana == 3:
    print(f"\nO dia será {YELLOW}terça-feira{WHITE}!!!\n")
elif dia_semana == 4:
    print(f"\nO dia será {BLUE}quarta-feira{WHITE}!!!\n")
elif dia_semana == 5:
    print(f"\nO dia será {GREEN}quinta-feira{WHITE}!!!\n")
elif dia_semana == 6:
    print(f"\nO dia será {GREEN}sexta-feira{WHITE}!!!\n")
elif dia_semana == 7:
    print(f"\nO dia será {GREEN}Sábado{WHITE}!!!\n")
else:
    print(f"\nValor {RED}Inválido{WHITE}...\n")
