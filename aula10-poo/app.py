from aluno import Aluno
from disciplina import Disciplina

# Criar/estanciar um aluno
aluno1 = Aluno("João", "123456", "Ciência da Computaçao")

# Criar/estanciar duas disciplinas
dsa = Disciplina("Data Structure", "Alvaro")
model_lin = Disciplina("Modelagem Linear", "Rodolfo")

# Matricular o aluno nas disciplinas
aluno1.matricular(dsa)
aluno1.matricular(model_lin)

# Adicionar nota por disciplina
aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
print(aluno1.nota_por_disciplina)

# Calcular média por matéria

print(aluno1.calcular_media_d(dsa))
print(aluno1.calcular_media_d(model_lin))
