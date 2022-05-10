import time  # importando biblioteca para colocar tempo antes de executar ação
import pyautogui  # biblioteca de automação do teclado
import pyperclip  # biblioteca de automação do mouse
import pandas as pd  # biblioteca para tratar dados

"""
Foi montado um automatizador de tarefas para buscar um arquivo no google drive,
baixar ele e ler, após identificar 2 valores sendo eles "Faturamento" e "Quantidade"
após abrir uma aba no navegador acessando meu email ja logado no chrome
e enviando para um email com assunto e texto com formatação informando os 
dados no arquivo consultados, após execução da tarefa principal, fecho as abas 
do navegador e encerra a execução.
"""

# IMPORTANTE
""" 
este códico só funciona para mim, ou seja tem que adaptar conforme o uso, pois a 
minha posição de tela (x= e y=) é diferente da sua.
"""

#comando para pegar a posição do mouse e poder ajustar conforme a tela de uso

#time.sleep(3)
#pyautogui.position()
#print(pyautogui.position())



#abrir chrome
pyautogui.hotkey("winleft")
time.sleep(1)
pyautogui.write("google")
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.click(x=405, y=430)

pyautogui.PAUSE = 2  # aguardar antes de executar cada passo do pyautogui

# passo 1: entrar no sistema da empresa(neste caso link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(3)  # aguarda (3) segundos para entrar na pasta selecionada

# passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta exportar)
pyautogui.click(x=-1046, y=653, clicks=2)  # 2 cliques para entrar na pasta

# passo 3: Exportar/fazer Download da Base de Dados
time.sleep(2)
pyautogui.click(x=-939, y=614)  # seleciona o arquivo da pasta
time.sleep(2)
pyautogui.click(x=-211, y=187)  # abre opções do arquivo
time.sleep(2)
pyautogui.click(x=-456, y=625)  # clica em fazer download
time.sleep(7)  # aguarda o download finalizar

# passo 4: Importar a base de dados para Python
# localização dada conforme minha organização de arquivos e nome usuário
tabela = pd.read_excel(r"C:\Users\jonat\Downloads\Vendas - Dez.xlsx")

#  passo 5: Calcular os indicadores
quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()

# passo 6: Enviar um email para responsavel com o relatório
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=-197, y=135)
time.sleep(3)
pyautogui.click(x=-1285, y=280)
time.sleep(3)

#  inserindo email para enviar
pyautogui.write("alunojygm@gmail.com")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
time.sleep(1)

#  escrevendo assunto
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")  # sair do assunto
time.sleep(1)

#  Escrevendo corpo do email
texto = f"""
prezados, bom dia!

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade total de venda foi de {quantidade:,}
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

#  enviar o email
pyautogui.hotkey("ctrl", "enter")

#encerrando processo
time.sleep(2)
pyautogui.hotkey("ctrl", "w")
pyautogui.hotkey("ctrl", "w")



