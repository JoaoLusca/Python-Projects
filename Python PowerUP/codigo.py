#====Passo a passo do programa====
#1º: Entrar no sistema da empresa
#2º: Fazer login
#3º: Abrir a base de dados
#4º: Cadastrar 1 produto
#5º: Repetir o passo 4 até terminar a base de dados
#=================================

import pyautogui
import time

# pyautogui.click --> Clica em um local específico da tela
# pyautogui.write --> Escreve um texto
# pyautogui.press --> Pressiona uma tecla
# pyautogui.hotkey --> Pressiona uma combinação de teclas

pyautogui.PAUSE = 0.5 # Faz o programa esperar 0.5s segundo entre cada comando
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
user = 'pythonimpressionador@gmail.com'
pswd = 'sua senha'

#1º: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

# --> inserindo o link do sistema da empresa e entrando
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2) # Esperando a página carregar

# 2º: Fazer login
# --> Fazendo o login

    ## Em alguns sites, é necessário clicar no campo de email para que ele seja shttps://dlp.hashtagtreinamentos.com/python/intensivao/login
    # elecionado e o texto possa ser escrito. Em outros, basta escrever o texto que o campo é selecionado automaticamente ou então apertar tab. O mesmo vale para o campo de senha. Por isso, é importante testar o código para ver se é necessário clicar ou não nos campos.
pyautogui.click(x=291, y=374) # Clicando no campo de email
pyautogui.write(user) # Escrevendo o email  
pyautogui.press("tab") # Passando para o campo de senha
pyautogui.write(pswd) # Escrevendo a senha
pyautogui.press("tab") # passando paa o botão de login
pyautogui.press("enter") # Clicando no botão de login
time.sleep(2) # Esperando a página carregar

# 3º: Abrir a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

#4º: Cadastrar 1 produto
for linha in tabela.index: #index é o número da linha

    pyautogui.click(x=238, y=271) # Passando para o campo de cadastro

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") 

    # observação
    observacao = tabela.loc[linha, "obs"]

    if str(observacao) != "nan":  # verifica se não está vazio
        pyautogui.write(str(observacao))
    else:
        pyautogui.write("NaN") # caso esteja vazio, escreve "NaN" para não dar erro no cadastro

    pyautogui.press("tab")  

    pyautogui.press("enter") # Clicando no botão de cadastrar
    time.sleep(1) # Esperando o cadastro ser processado

    pyautogui.scroll(10000) # Rolando a tela para cima para o campo de cadastro ficar visível