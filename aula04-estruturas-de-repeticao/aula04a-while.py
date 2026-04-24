# # Exemplo básico
# cp = 0
#
# while cp < 3:
#     print(f"Produto {cp}")
#     cp += 1
#
# # While decrescente de 4 até 1
# i = 4
#
# while i > 0:
#     print(i)
#     i -= 1
#
# # Repetição com entrada do usuário
# jogar = "sim"
#
# while jogar.lower() == "sim":
#     print("Iniciar ou repetir o jogo")
#     jogar = input("Deseja jogar novamente? ")

i = 0

while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")