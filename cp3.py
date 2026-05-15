temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_maior_risco = 0
max_criticos = -1

for i in range(len(temperaturas)):
    soma_sala = 0
    criticos_sala = 0

    for j in range(len(temperaturas[i])):
        temp = temperaturas[i][j]
        soma_sala += temp

        if temp >= 33:
            criticos_sala += 1

    media = soma_sala / len(temperaturas[i])

    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {criticos_sala}")
    print()

    if criticos_sala > max_criticos:
        max_criticos = criticos_sala
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")
