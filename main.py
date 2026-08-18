class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e minha matrícula é {self.matricula}."

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e eu ensino {self.disciplina}."

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.professor = None

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Aluno.")

    def definir_professor(self, professor):
        if isinstance(professor, Professor):
            self.professor = professor
        else:
            raise ValueError("O objeto definido deve ser uma instância da classe Professor.")

    def apresentar_turma(self):
        apresentacao = f"Turma: {self.nome}\n"
        apresentacao += "Professor: " + (self.professor.apresentar() if self.professor else "Nenhum professor definido") + "\n"
        apresentacao += "Alunos:\n"
        for aluno in self.alunos:
            apresentacao += aluno.apresentar() + "\n"
        return apresentacao

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def adicionar_turma(self, turma):
        if isinstance(turma, Turma):
            self.turmas.append(turma)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Turma.")

    def apresentar_escola(self):
        apresentacao = f"Escola: {self.nome}\n"
        for turma in self.turmas:
            apresentacao += turma.apresentar_turma() + "\n"
        return apresentacao

class SistemaEscolar:
    def __init__(self):
        self.escolas = []

    def adicionar_escola(self, escola):
        if isinstance(escola, Escola):
            self.escolas.append(escola)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Escola.")

    def apresentar_sistema(self):
        apresentacao = "Sistema Escolar:\n"
        for escola in self.escolas:
            apresentacao += escola.apresentar_escola() + "\n"
        return apresentacao

class Menu:
    def __init__(self):
        self.sistema = SistemaEscolar()

    def exibir_menu(self):
        while True:
            print("1. Adicionar Escola")
            print("2. Adicionar Turma")
            print("3. Adicionar Aluno")
            print("4. Adicionar Professor")
            print("5. Apresentar Sistema Escolar")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_escola()
            elif opcao == "2":
                self.adicionar_turma()
            elif opcao == "3":
                self.adicionar_aluno()
            elif opcao == "4":
                self.adicionar_professor()
            elif opcao == "5":
                print(self.sistema.apresentar_sistema())
            elif opcao == "6":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_escola(self):
        nome = input("Digite o nome da escola: ")
        escola = Escola(nome)
        self.sistema.adicionar_escola(escola)
        print(f"Escola '{nome}' adicionada com sucesso.")

    def adicionar_turma(self):
        nome_escola = input("Digite o nome da escola: ")
        escola = next((e for e in self.sistema.escolas if e.nome == nome_escola), None)
        if escola:
            nome_turma = input("Digite o nome da turma: ")
            turma = Turma(nome_turma)
            escola.adicionar_turma(turma)
            print(f"Turma '{nome_turma}' adicionada à escola '{nome_escola}'.")
        else:
            print(f"Escola '{nome_escola}' não encontrada.")

    def adicionar_aluno(self):
        nome_escola = input("Digite o nome da escola: ")
        escola = next((e for e in self.sistema.escolas if e.nome == nome_escola), None)
        if escola:
            nome_turma = input("Digite o nome da turma: ")
            turma = next((t for t in escola.turmas if t.nome == nome_turma), None)
            if turma:
                nome_aluno = input("Digite o nome do aluno: ")
                idade_aluno = int(input("Digite a idade do aluno: "))
                matricula_aluno = input("Digite a matrícula do aluno: ")
                aluno = Aluno(nome_aluno, idade_aluno, matricula_aluno)
                turma.adicionar_aluno(aluno)
                print(f"Aluno '{nome_aluno}' adicionado à turma '{nome_turma}'.")
            else:
                print(f"Turma '{nome_turma}' não encontrada na escola '{nome_escola}'.")
    def adicionar_professor(self):
        nome_escola = input("Digite o nome da escola: ")
        escola = next((e for e in self.sistema.escolas if e.nome == nome_escola), None)
        if escola:
            nome_turma = input("Digite o nome da turma: ")
            turma = next((t for t in escola.turmas if t.nome == nome_turma), None)
            if turma:
                nome_professor = input("Digite o nome do professor: ")
                idade_professor = int(input("Digite a idade do professor: "))
                disciplina_professor = input("Digite a disciplina do professor: ")
                professor = Professor(nome_professor, idade_professor, disciplina_professor)
                turma.definir_professor(professor)
                print(f"Professor '{nome_professor}' definido para a turma '{nome_turma}'.")
            else:
                print(f"Turma '{nome_turma}' não encontrada na escola '{nome_escola}'.")
