# Projeto criado com o curso intensivo de python da empowerdata.
# Programa realiza uma simples ação de enviar email de forma automatica
# com os dados de uma ação desejada

# Adição das bibliotecas que serão usadas no projeto.
import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

# campos de entrada para entrada de dados referente a ação.
dados = input("Qual o ticker da ação?\n")
dt_inicial = input("Qual o período inicial desejado? (formatação desejada: ano-mês-dia)\n")
dt_final = input("Qual período final desejado? (formatação desejada: ano-mês-dia)\n")

# campo da tabela que recebe os dados e datas conforme fornecido pelo usuario.
tabela = yfinance.Ticker(dados).history(start=dt_inicial, end=dt_final)

fechamento = tabela.Close   # aqui trabalhamos com o fechamento da tabela.

# aqui mostra a tabela para o usuario.
print("Tabela dos dados abaixo: ")
print(tabela)

# campos com os dados que serão impressos no Gmail
assunto = input("Qual o assunto do email?\n")
destinatario = input("Para qual destinatário será enviado?\n")
mensagem = f"""
Bom dia,

Segue abaixo as análises da ação do período solicitado: a :{dados}


Cotação máxima: R${round(fechamento.max(), 2)}

Cotação mínima: R${round(fechamento.min(), 2)}

Valor médio: R${round(fechamento.mean(), 2)}
"""

# abre o navegador com a pagina do google e espera 7 segundos para que a pagina seja carregada.
webbrowser.open("https://www.gmail.com")
time.sleep(7)

pyautogui.PAUSE = 1 # define um tempo de 1 segundo para cada ação do pyautogui.

pyautogui.click(x=86, y=160) # coordenadas para o mouse clicar em um monitor 1080p.

pyperclip.copy(destinatario)    # comando que copia para o cntrl + c o argumento.
pyautogui.hotkey("ctrl", "v")   # método hotkey ativa a ação do teclado.
pyautogui.hotkey("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1265, y=989)