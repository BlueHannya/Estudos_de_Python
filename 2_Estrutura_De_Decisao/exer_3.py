"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, 
Sexo Inválido."""

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

genero = input(f"""\nPara selecionar seu gênero insira {PURPLE}'F'{WHITE} para {PURPLE}Feminino{WHITE}, ou {GREEN}'M'{WHITE} para
{GREEN}Masculino{WHITE}: """)

if genero == "F" or genero == "f":
    print(f"\nSeu gênero é {PURPLE}Feminino{WHITE}.\n")
elif genero == "M" or genero == "m":
    print(f"\nSeu gênero é {GREEN}Masculino{WHITE}.\n")
else:
    print(f"\nNão identificamos seu {RED}gênero{WHITE}...\n")