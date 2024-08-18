#Cores

"""RESET = "\033[m"
RED =  "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
TEAL = "\033[36m"
GRAY = "\033[37m"""

RESET = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m";
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

# Comportamento de cores

"""Usamos o padrão de cores 'ANSI' ao qual começa com o código '\033[' é definido esses códigos para tipo de texto;cor;fundo 0;0;0m 
onde cada um tem seu número e propósito para personalizar o texto de forma prática e fácil"""


#Teste

print(f"\n{BLUE}aaaaa AAAAAAAAA AAAAAAA {RESET}aaaaaaaaa AAaaAAAAAaaa\n")

# Texto com f-string e cores ANSI

nome = "Maria"
mensagem = f"{RED}[{nome}]{RESET} está aprendendo Python!\n"

print(mensagem)