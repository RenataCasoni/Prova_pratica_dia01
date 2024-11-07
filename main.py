def importar_dados():
    alocacoes ={}

    with open("alocacoes.txt", "r") as file:
        for line in file:
            nome_funcionario, nome_projeto = line.strip().split(';')
            alocacoes[nome_funcionario] = nome_funcionario
            alocacoes[nome_projeto] = nome_projeto

    projetos = {}
    with open("projetos.txt", "r") as file:
        texto = []
        for line in file:
            if line[0:2] != "##":
                texto += [linha.strip().split(" ")]
            nome, departamento_responsavel = line.strip().split(';')
            projetos[nome] = nome
            projetos[departamento_responsavel] = departamento_responsavel

    departamentos = {}
    with open("departamentos.txt", "r") as file:
        for line in file:
            nome, qtd_funcionarios = line.strip().split(';')
            departamentos[nome] = nome
            departamentos[qtd_funcionarios] = qtd_funcionarios

    funcionarios = {}
    with open("funcionarios.txt", "r") as file:
        for line in file:
            nome, departamentos, AnosExperiencia = line.strip().split(';')
            funcionarios[nome] = nome
            funcionarios[qtd_funcionarios] = qtd_funcionarios
            funcionarios[nome] = AnosExperiencia

    return alocacoes, projetos, departamentos, funcionarios

alocacoes, projetos, departamentos, funcionarios = importar_dados()

print("Projetos:", projetos)
#print("Alocações:", alocacoes)
#print("Alocações:", departamentos)
#print("Alocações:", funcionarios)