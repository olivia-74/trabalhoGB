import csv

arquivoCSV = open('gatos.csv',encoding='utf-8')
leitor = csv.reader(arquivoCSV,delimiter=';')
dados = list(leitor) #aqui já temos uma tabela, mas apenas com strings
dadosONG = [] # dadosONG é a matriz que vai mesmo armazenar nossos dados para as consultas
listaMenu = [ # lista das opcoes do menu
            "1) Cadastrar felino",
            "2) Alterar status de felino", 
            "3) Consultar informações sobre felino", 
            "4) Apresentar estatísticas gerais", 
            "5) Filtragem de dados", 
            "6) Salvar", 
            "7) Sair do programa"
        ]


# funcoes -------------------

def OperacoesMenu (listaMenu): # dividir funcoes!!

    print("Menu:")
    for i in range (len(listaMenu)):
        print(listaMenu[i])

    while True:
        opcao = int(input("Insira o numero da acao que deseja realizar: ")) # opcao do menu selecionada pelo usuario 
        if opcao in [1, 2, 3, 4, 5, 6, 7]: # condicao q verifica se a opcao e valida
            if opcao == 1:
                CadastrarFelino()
            elif opcao == 2:
                AlterarStatus()
            elif opcao == 3:
                ConsultarInformacoes()
            elif opcao == 4:
                EstatisticasGerais()
            elif opcao == 5:
                FiltragemDados()
            elif opcao == 6:
                Salvar()
            elif opcao == 7: #esse nao precisa de funcao
                Salvar()
                print("Saindo...")
                break
        else: 
            print("Opção inválida!")

# funcao opcao 1
def CadastrarFelino():
    oie

# funcao opcao 2
def AlterarStatus():
    oie

# funcao opcao 3
def ConsultarInformacoes():
    oie

# funcao opcao 4
def EstatisticasGerais():
    oie

# funcao opcao 5
def FiltragemDados():
    oie

# funcao opcao 6
def Salvar():
    oie

print(dados)


# Preenchendo dadosONG, fazendo as conversões de tipo necessárias
#percorrer, linha a linha, nossa matriz (tabela) de dados
for i in range(len(dados)): #percorrendo as linhas (esse csv não tem cabeçalho)
    linha = [] #linha auxiliar
    for j in range(len(dados[0])): #percorrendo as colunas
        if j == 2: #terceira coluna é a idade
            linha.append(int(dados[i][j]))
        else:
            linha.append(dados[i][j])
    dadosONG.append(linha)


def Main():
    OperacoesMenu(listaMenu)

print(Main())