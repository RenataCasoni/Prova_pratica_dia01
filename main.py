def importar_dados():
    alocacoes ={}

    with open("alocacoes.txt", "r") as file:
        for line in file:
            if(not line.startswith('NomeFuncionario')):
             nome_funcionario, nome_projeto = line.strip().split(';')
             alocacoes[nome_funcionario] = nome_funcionario
             alocacoes[nome_funcionario] = nome_projeto

    projetos = {}
    with open("projetos.txt", "r") as file:
        for line in file:
            if(not line.startswith('Nome')):
             nome, departamento_responsavel = line.strip().split(';')
             projetos[nome] = nome
             projetos[nome] = departamento_responsavel

    departamentos = {}
    with open("departamentos.txt", "r") as file:
        for line in file:
            if(not line.startswith('Nome')):
             nomedep, qtd_funcionarios = line.strip().split(';')
             departamentos[nomedep] = nomedep
             departamentos[nomedep] = qtd_funcionarios

    funcionarios = {}
    with open("funcionarios.txt", "r") as file:
        for line in file:
            if(not line.startswith('Nome')):
             nome, departamentos, AnosExperiencia = line.strip().split(';')
             funcionarios[nome] = nome
             funcionarios[nome] = qtd_funcionarios
             funcionarios[nome] = AnosExperiencia

    return alocacoes, projetos, departamentos, funcionarios

alocacoes, projetos, departamentos, funcionarios = importar_dados()

print("Projetos:", projetos)
print("Alocações:", alocacoes)
print("Departamentos:", departamentos)
print("Funcionarios:", funcionarios)