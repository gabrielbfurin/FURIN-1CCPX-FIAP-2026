duplas = ["Ana", "Maria", "Vini", "Mat"]

for i in range(len(duplas)):
    for j in range(i + 1, len(duplas)):
            print(f"Possiveis duplas: {duplas[i]} e {duplas[j]}")