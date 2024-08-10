import yfinance
import pyautogui
import pyperclip
import webbrowser
import time


dados = input("Qual o ticker da ação?\n")
dt_inicial = input("Qual o período inicial desejado? (formatação desejada: ano-mês-dia)\n")
dt_final = input("Qual período final desejado? (formatação desejada: ano-mês-dia)\n")

tabela = yfinance.Ticker(dados).history(start=dt_inicial, end=dt_final)

fechamento = tabela.Close

print("Tabela dos dados abaixo: ")
print(tabela)

assunto = input("Qual o assunto do email?\n")
destinatario = input("Para qual destinatário será enviado?\n")
mensagem = f"""
Bom dia,

Segue abaixo as análises da ação do período solicitado: a :{dados}


Cotação máxima: R${round(fechamento.max(), 2)}

Cotação mínima: R${round(fechamento.min(), 2)}

Valor médio: R${round(fechamento.mean(), 2)}
"""


webbrowser.open("https://www.gmail.com")
time.sleep(7)

pyautogui.PAUSE = 1

pyautogui.click(x=86, y=160)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1265, y=989)