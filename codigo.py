# passo 1: Entrar no  sistema da empresa -https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# passo 2: Fazer login
pyautogui.click(x=1206, y=392)
pyautogui.write("fabioh2mteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("fh2m546")
pyautogui.press("enter")


# passo 3: Importar a base de dados
#pip install pandas
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)


#print(tabela)=>mostra a tabela abaixo, no terminal.

# passo 4: Cadastrar 1 produto
pyautogui.press("tab")

#linha = 0 (com essa variável, ele executa só a 1a. linha q é a zero) abaixo, vou indentar para preenchimento de todos os dados até terminar a tabela.
for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    #abaixo, se não houver dados no obs, ele vai pular.
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # passo 5: Repetir o processo de cadastro até acabar os produtos

    pyautogui.scroll(5000)
    pyautogui.click(x=1200, y=288)


