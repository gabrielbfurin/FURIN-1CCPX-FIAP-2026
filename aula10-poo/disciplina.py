class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | Prof: {self.professor}")

model_mat = Disciplina(nome="MMC", professor="Igor")
print(model_mat)
model_mat.exibir_infos()