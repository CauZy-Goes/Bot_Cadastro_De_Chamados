import time
import pyautogui
import pandas
import posicoes_elementos

def configurarRobo():
    #tempo de espera base
    pyautogui.PAUSE = 0.3

def entrarNavegador():
    #entrando no navegador
    pyautogui.press("win")
    pyautogui.write("edge")
    pyautogui.press("enter")

def acessarSite(linkSite):
    #acessando site para cadastro dos chamados
    time.sleep(1)
    pyautogui.hotkey("ctrl","t")
    time.sleep(1.5)
    pyautogui.write(linkSite)
    pyautogui.press("enter")        

def fazerAutenticacao(login,senha):
    #fazer autenticação
    time.sleep(1.5)
    pyautogui.press("tab")
    pyautogui.write(login)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")

def acessarCadastro():
    #acessar espaco de cadastro
    time.sleep(1.5)
    for i in range(5):
        pyautogui.press("tab")
    pyautogui.press("enter")

def cadastrarChamadosDoCsv(nomeDoArquivo):
    #cadastrar todos os chamados da lista
    tabela = pandas.read_csv(nomeDoArquivo)

    #cadastra todos os chamados 
    for linha in tabela.index:
        pyautogui.click(x=417, y=254)

        #cadastra o cliente
        cliente = str(tabela.loc[linha,"cliente"]).lower()
        posicao_cliente = posicoes_elementos.clientes.get(cliente)
        for nSetasParaBaixo in range(posicao_cliente):
            pyautogui.press('down')
        pyautogui.press("enter")
        pyautogui.press("tab")

        #cadastra o servico
        servico = str(tabela.loc[linha,"servico"]).lower()
        posicao_servico = posicoes_elementos.servicos.get(servico)


        #ajustar o select
        pyautogui.PAUSE = 0.1
        for nSetasParaCima in range(20):
            pyautogui.press('up')
        pyautogui.PAUSE = 0.3

        for nSetasParaBaixo in range(posicao_servico):
            pyautogui.press('down')
        pyautogui.press("tab")

        #pula a area de status
        pyautogui.press("tab")

        #escreve a descricao do chamado
        descricao = str(tabela.loc[linha,"descricao"])
        pyautogui.write(descricao)

        #cadastra
        pyautogui.press("tab")
        pyautogui.press("enter")
    