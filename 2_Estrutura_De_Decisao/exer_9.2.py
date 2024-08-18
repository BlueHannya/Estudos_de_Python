# Já a segunda a função '.sorted()'

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]

numeros_ordenados = sorted(numeros, reverse=True)

""" Nela criamos uma variavel (objeto) para não alterarmos a lista original, assim mudando sua ordem, no caso 
'sorted(numeros, reverse=True)' fazemos a de forma decrescente.
Podemos  """

print(f"\nOs números na ordem {YELLOW}decrescente{WHITE} ficam: {YELLOW}{numeros_ordenados}{WHITE}\n")

# Podemos fazer o uso de IFs e Elses mas ficará bem extenso, então as funções estão aqui para nos ajudar