import main as Escola

sistema = Escola.SistemaEscolar()

sistema.adicionar_escola(Escola.Escola("Escola A"))

turma1 = Escola.Turma("Turma 1")
professor1 = Escola.Professor("Professor A", 40, "Matemática")

aluno1 = Escola.Aluno("Aluno 1", 20, "Matemática")
aluno2 = Escola.Aluno("Aluno 2", 21, "Matemática")

turma1.definir_professor(professor1)
turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)

sistema.escolas[0].adicionar_turma(turma1)

#usando o método apresentar_sistema para exibir a estrutura completa do sistema escolar
print(sistema.apresentar_sistema())
