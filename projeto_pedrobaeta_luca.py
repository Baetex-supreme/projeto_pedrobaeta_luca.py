
# SISTEMA DE CADASTRO DE ALUNOS
# Projeto Final - AV1 de Lógica de Programação

# Lista inicial com três alunos cadastrados
alunos = [
    {
        "matricula": 101,
        "nome": "João Silva",
        "turma": "1A",
        "media": 8.5,
        "idade": 15
    },
    {
        "matricula": 102,
        "nome": "Maria Santos",
        "turma": "1B",
        "media": 9.0,
        "idade": 16
    },
    {
        "matricula": 103,
        "nome": "Pedro Oliveira",
        "turma": "1A",
        "media": 7.5,
        "idade": 15
    }
]


# Função para exibir o menu
def exibir_menu():
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")


# Função para cadastrar alunos
def cadastrar(alunos):
    print("\n--- CADASTRAR ALUNO ---")

    try:
        matricula = int(input("Digite a matrícula: "))

        # Verifica se a matrícula já existe
        for aluno in alunos:
            if aluno["matricula"] == matricula:
                print("Essa matrícula já está cadastrada!")
                return

        nome = input("Digite o nome: ").strip()
        turma = input("Digite a turma: ").strip()
        media = float(input("Digite a média: "))
        idade = int(input("Digite a idade: "))

        if not nome or not turma:
            print("Nome e turma não podem ficar vazios!")
            return

        if media < 0 or media > 10 or idade <= 0:
            print("Média ou idade inválida!")
            return

        novo_aluno = {
            "matricula": matricula,
            "nome": nome,
            "turma": turma,
            "media": media,
            "idade": idade
        }

        alunos.append(novo_aluno)
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Erro! Digite números nos campos numéricos.")


# Função para listar todos os alunos
def listar(alunos):
    print("\n--- LISTA DE ALUNOS ---")

    if len(alunos) == 0:
        print("Não existem alunos cadastrados.")
        return

    for aluno in alunos:
        print("-------------------------")
        print("Matrícula:", aluno["matricula"])
        print("Nome:", aluno["nome"])
        print("Turma:", aluno["turma"])
        print("Média:", aluno["media"])
        print("Idade:", aluno["idade"])


# Função para buscar um aluno
def buscar(alunos):
    print("\n--- BUSCAR ALUNO ---")

    if len(alunos) == 0:
        print("Não existem alunos cadastrados.")
        return

    try:
        matricula = int(input("Digite a matrícula do aluno: "))

        encontrado = False
        comparacoes = 0

        # Busca sequencial
        for aluno in alunos:
            comparacoes += 1

            if aluno["matricula"] == matricula:
                print("\nAluno encontrado!")
                print("Nome:", aluno["nome"])
                print("Matrícula:", aluno["matricula"])
                print("Turma:", aluno["turma"])
                print("Média:", aluno["media"])
                print("Idade:", aluno["idade"])

                encontrado = True
                break

        if encontrado == False:
            print("Aluno não encontrado!")

        print("Comparações realizadas:", comparacoes)

    except ValueError:
        print("Digite uma matrícula válida!")


# Função para remover um aluno
def remover(alunos):
    print("\n--- REMOVER ALUNO ---")

    if len(alunos) == 0:
        print("Não existem alunos cadastrados.")
        return

    try:
        matricula = int(input("Digite a matrícula que deseja remover: "))

        for i in range(len(alunos)):
            if alunos[i]["matricula"] == matricula:
                aluno_removido = alunos.pop(i)
                print("Aluno", aluno_removido["nome"],
                      "removido com sucesso!")
                return

        print("Matrícula não encontrada!")

    except ValueError:
        print("Digite uma matrícula válida!")


# Programa principal
while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar(alunos)

    elif opcao == "2":
        listar(alunos)

    elif opcao == "3":
        buscar(alunos)

    elif opcao == "4":
        remover(alunos)

    elif opcao == "5":
        print("Programa encerrado. Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
