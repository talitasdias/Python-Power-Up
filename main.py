import pyautogui as py
import pandas as pd
from time import sleep
# Passo 1 - Entrar no sistema da empresa
    # site: https://dlp.hashtagtreinamentos.com/python/intensivao/login
py.PAUSE = 1
py.hotkey('win', 's')
py.write('chrome')
py.press('enter')
sleep(4)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
py.write(link)
py.press('enter')

# Passo 2 - Fazer login
sleep(3)
py.press('tab')
email = 'pythonimpressionador@gmail.com'
senha = 'minha senha'
py.write(email)
py.press('tab')
py.write(senha)
py.press('tab')
py.press('enter')

# Passo 3 - Importar a base de dados
tabela = pd.read_csv('produtos.csv')

# Passo 4 - Cadastrar produtos e repetir até acabar a base de dados
py.press('tab')
for linha in tabela.index:
    #codigo
    py.write(str(tabela.loc[linha, 'codigo']))
    py.press('tab')
    #marca
    py.write(tabela.loc[linha, 'marca'])
    py.press('tab')
    #tipo
    py.write(tabela.loc[linha, 'tipo'])
    py.press('tab')
    #categoria
    py.write(str(tabela.loc[linha, 'categoria']))
    py.press('tab')
    #preco_unitario
    py.write(str(tabela.loc[linha, 'preco_unitario']))
    py.press('tab')
    #custo
    py.write(str(tabela.loc[linha, 'custo']))
    py.press('tab')
    #obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        py.write(str(obs))
    py.press('tab')
    py.press('enter')
    sleep(2)
    py.press('F5')
    sleep(4)
    py.press('tab')
