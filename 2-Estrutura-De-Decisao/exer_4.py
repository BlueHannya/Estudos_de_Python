"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

letra = input("\nDigite uma letra: ")

# Para verificar se letra é um número, você pode usar o método '.isdigit()'.

if letra.isdigit():
    print(f"\nIsso é uma letra onde {RED}miserável{WHITE}?...\n")
elif letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print(f"\nVocê usou uma vogal: '{GREEN}{letra}{WHITE}'\n")
else:
    print(f"\nVocê usou uma consoante: {YELLOW}{letra}{WHITE}\n")
