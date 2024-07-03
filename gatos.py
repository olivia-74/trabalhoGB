import csv

# Função para carregar os dados do arquivo CSV para uma lista de listas
def carregar_dados():
    with open('gatos.csv', encoding='utf-8') as arquivoCSV:
        leitor = csv.reader(arquivoCSV, delimiter=';')
        dados = list(leitor) # lendo as listas do csv
    dadosONG = []
    # percorre a matriz
    for l in range(len(dados)):
        linha = []
        for c in range(len(dados[0])):
            if c == 2: # colocando int para o valor idade
                linha.append(int(dados[l][c]))
            else:
                linha.append(dados[l][c])
        dadosONG.append(linha) # coloca as informacoes no array
    return dadosONG

# funcao para as operacoes do menu
def OperacoesMenu(listaMenu, dadosONG):
    while True:
        print("Menu:") # printa a lista de itens do menu definida no main
        for i in range(len(listaMenu)):
            print(listaMenu[i])

        opcao = int(input("Insira o número da ação que deseja realizar: "))
        if opcao in range(1, 8): # executa a funcao respectiva ao input do usuario
            if opcao == 1:
                CadastrarFelino(dadosONG)
            elif opcao == 2:
                AlterarStatus(dadosONG)
            elif opcao == 3:
                ConsultarInformacoes(dadosONG)
            elif opcao == 4:
                EstatisticasGerais(dadosONG)
            elif opcao == 5:
                FiltragemDados(dadosONG)
            elif opcao == 6:
                Salvar(dadosONG)
            elif opcao == 7:
                Salvar(dadosONG)
                print("Saindo...")
                break
        else:
            print("Opção inválida!")
        print()


# função opção 1
def CadastrarFelino(dadosONG): 
    print("Cadastro de Novo Felino")
    nome = input("Nome: ")
    sexo = input("Sexo (M/F): ")
    idade = int(input("Idade: "))
    raca = input("Raça: ")
    cor = input("Cor Predominante: ")
    castrado = input("Castrado (Sim/Não): ")
    fiv = input("FIV+ (Sim/Não): ")
    felv = input("FELV+ (Sim/Não): ")
    dataResgate = input("Data de Resgate (dd/mm/aaaa): ")
    adotado = input("Adotado (Sim/Não): ")
    larTemporario = input("Lar Temporário (Sim/Não): ")
    dataAdocao = input("Data de Adoção/Hospedagem (dd/mm/aaaa) ou '-': ")
    tutor = input("Nome do Tutor ou '-': ")
    contatoTutor = input("Telefone do Adotante ou '-': ")
    dataUltimaVacina = input("Data da última vacina (dd/mm/aaaa) ou '-': ")
    dataDesvermifugacao = input("Data da última desvermifugação (dd/mm/aaaa) ou '-': ")
    dataAntipulgas = input("Data do último antipulgas (dd/mm/aaaa) ou '-': ")
    informacoesExtras = input("Informações extras: ")

    # armazenando as informacoes sobre o felino
    novoFelino = [
        nome, sexo, idade, raca, cor, castrado, fiv, felv, dataResgate, adotado, larTemporario,
        dataAdocao, tutor, contatoTutor, dataUltimaVacina, dataDesvermifugacao, dataAntipulgas, informacoesExtras
    ]

    dadosONG.append(novoFelino) # coloca a nova lista na matriz
    print("Felino cadastrado com sucesso!")


# função opção 2
def AlterarStatus(dadosONG): # altera informacoes de um felino ja cadastrado
    print("Alteração de Status de Felino")
    for index, felino in enumerate(dadosONG): # lista todos os felinos cadastrados
        print(f"{index + 1}) {felino[0]}")

    opcao = int(input("Escolha o felino pelo número: ")) - 1

    if 0 <= opcao < len(dadosONG): # imprime todas as informacoes do felino
        felino = dadosONG[opcao]
        titulos = [
            "Nome", "Sexo", "Idade", "Raça", "Cor Predominante", "Castrado", "FIV+", "FELV+", "Data de Resgate", 
            "Adotado", "Lar Temporário", "Data de Adoção/Hospedagem", "Nome do Tutor", "Telefone do Adotante", 
            "Data da Última Vacina", "Data da Última Desvermifugação", "Data do Último Antipulgas", "Informações Extras"
        ]
        print(f"Informações do felino {felino[0]}:") 
        for titulo, info in zip(titulos, felino): # zip itera sobre duas listas simultaneamente
            print(f"{titulo}: {info}")

        while True: # loop para escolher o que alterar
            campo = int(input("Escolha o campo para alterar (ou 0 para sair): ")) - 1 
            if campo == -1: #sai do loop
                break
            if 0 <= campo < len(felino): # verifica se o valor do input e valido
                novoValor = input(f"Novo valor para {felino[campo]}: ")
                felino[campo] = novoValor # altera o valor do campo escolhido
            else:
                print("Campo inválido!")
        print("Informações atualizadas!")
    else:
        print("Felino não encontrado!")


# função opção 3
def ConsultarInformacoes(dadosONG):  # imprime as informacoes do felino escolhido
    print("Consulta de Informações sobre Felino")
    for index, felino in enumerate(dadosONG):
        print(f"{index + 1}) {felino[0]}") # lista todos os felinos cadastrados

    opcao = int(input("Escolha o felino pelo número: ")) - 1

    if 0 <= opcao < len(dadosONG):
        felino = dadosONG[opcao]
        titulos = [ # "titulos" correspondentes a cada informacao
            "Nome", "Sexo", "Idade", "Raça", "Cor Predominante", "Castrado", "FIV+", "FELV+", "Data de Resgate", 
            "Adotado", "Lar Temporário", "Data de Adoção/Hospedagem", "Nome do Tutor", "Telefone do Adotante", 
            "Data da Última Vacina", "Data da Última Desvermifugação", "Data do Último Antipulgas", "Informações Extras"
        ]
        print(f"Informações do felino {felino[0]}:")
        for titulo, info in zip(titulos, felino): # zip itera sobre duas listas simultaneamente
            print(f"{titulo}: {info}")
    else:
        print("Felino não encontrado!")

# função opção 4
def EstatisticasGerais(dadosONG): # estatisticas da base de dados
    totalFelinos = len(dadosONG) # quantidade de linhas da matriz = qtd de gatos
    totalMachos = sum(1 for felino in dadosONG if felino[1] == "M") # ve o sexo de acordo com a coluna 2
    totalFemeas = totalFelinos - totalMachos 
    totalAdotados = sum(1 for felino in dadosONG if felino[9] == "Sim") # ve o status de adocao na coluna 10
    totalNaoAdotados = totalFelinos - totalAdotados

    fivNeg = sum(1 for felino in dadosONG if felino[6] == "Não") 
    fivPos = totalFelinos - fivNeg
    felvNeg = sum(1 for felino in dadosONG if felino[7] == "Não")
    felvPos = totalFelinos - felvNeg
    fivFevPos = sum(1 for felino in dadosONG if felino[6] == "Sim" and felino[7] == "Sim")

    # imprime as informacoes em porcentagem
    print(f"Total de felinos: {totalFelinos}")
    print(f"Machos: {totalMachos} ({totalMachos / totalFelinos:.2%})")
    print(f"Fêmeas: {totalFemeas} ({totalFemeas / totalFelinos:.2%})")
    print(f"Adotados: {totalAdotados} ({totalAdotados / totalFelinos:.2%})")
    print(f"Não Adotados: {totalNaoAdotados} ({totalNaoAdotados / totalFelinos:.2%})")
    print(f"FIV-: {fivNeg} ({fivNeg / totalFelinos:.2%})")
    print(f"FIV+: {fivPos} ({fivPos / totalFelinos:.2%})")
    print(f"FELV-: {felvNeg} ({felvNeg / totalFelinos:.2%})")
    print(f"FELV+: {felvPos} ({felvPos / totalFelinos:.2%})")
    print(f"FIV+ e FELV+: {fivFevPos} ({fivFevPos / totalFelinos:.2%})")


# funcao opcao 5
def FiltragemDados(dadosONG): # filtra os dados os gatos resgatados ou adotados em determinado periodo (nao ta 100%)
    print("Filtragem de Dados")
    print("1) Gatos resgatados por período")
    print("2) Gatos adotados por período")
    opcao = int(input("Escolha a opção de filtragem: "))

    if opcao == 1:
        anoInicio = int(input("Ano de início: "))
        anoFim = int(input("Ano de fim: "))
        resgatados = [felino for felino in dadosONG if anoInicio <= int(felino[8].split('/')[2]) <= anoFim]
        for felino in resgatados:
            print(felino)
    elif opcao == 2:
        anoInicio = int(input("Ano de início: "))
        anoFim = int(input("Ano de fim: "))
        adotados = [felino for felino in dadosONG if felino[9] == "Sim" and anoInicio <= int(felino[10].split('/')[2]) <= anoFim]
        for felino in adotados:
            print(felino)
    else:
        print("Opção inválida!")


# função opção 6
def Salvar(dadosONG): # escreve uma linha no arquivo CSV para cada felino 
    with open('gatos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for felino in dadosONG:
            writer.writerow(felino)
    print("Dados salvos com sucesso!")


def Main():
    dadosONG = carregar_dados()
    listaMenu = [
        "1) Cadastrar felino",
        "2) Alterar status de felino",
        "3) Consultar informações sobre felino",
        "4) Apresentar estatísticas gerais",
        "5) Filtragem de dados",
        "6) Salvar",
        "7) Sair do programa"
    ]
    OperacoesMenu(listaMenu, dadosONG)


Main()
