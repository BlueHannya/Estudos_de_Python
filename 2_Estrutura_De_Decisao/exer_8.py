""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato. """

WHITE = "\033[m"; RED =  "\033[31m"; GREEN = "\033[32m"; YELLOW = "\033[33m"
BLUE = "\033[34m"; PURPLE = "\033[35m"; TEAL = "\033[36m"; GRAY = "\033[37m"

produto_1 = float(input("\nColoque o valor do 1 produto aqui: "))
produto_2 = float(input("Coloque o valor do 2 produto aqui: "))
produto_3 = float(input("Coloque o valor do 3 produto aqui: "))

produto_barato = min(produto_1, produto_2, produto_3)

print(f"\nO produto mais barato custa {TEAL}{produto_barato:.2f}{WHITE}\n")