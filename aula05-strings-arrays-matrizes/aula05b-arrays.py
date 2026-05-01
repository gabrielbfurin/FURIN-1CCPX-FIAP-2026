lista_frutas = ["Morango", "Maçâ", "Uva"]

# lista_frutas[0] = Morango
# lista_frutas[1] = Maçâ
# lista_frutas[2] = Uva

print(lista_frutas[1])
print()

lista_frutas.append("Melancia")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)