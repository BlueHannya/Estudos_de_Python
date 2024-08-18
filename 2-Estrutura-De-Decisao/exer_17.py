""" Faça um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto. """

WHITE = "\033[m"; RED = "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

ano = int(input("\n- Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"\nO ano {ano} {PURPLE}é bissexto{WHITE}.\n")
else:
    print(f"\nO ano {ano} {YELLOW}não é bissexto{WHITE}.\n")

# Um ano bissexto é um ano que tem 366 dias, em vez dos 365 dias habituais.
# Isso acontece porque fevereiro tem 29 dias em vez de 28. Os anos bissextos
# ocorrem a cada quatro anos, mas existem algumas exceções.

# Regras para determinar se um ano é bissexto:
# - Divisível por 4: O ano deve ser divisível por 4.
# - Exceção do século: Se o ano for divisível por 100, não é bissexto, a menos que:
# - Divisível por 400: Se o ano também for divisível por 400, então é bissexto.

# Exemplos:
# 2020: Bissexto (divisível por 4)
# 1900: Não bissexto (divisível por 100, mas não por 400)
# 2000: Bissexto (divisível por 400)
# Essas regras ajudam a manter o calendário em alinhamento com o ano solar."""
