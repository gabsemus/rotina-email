from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time

def enviar_email(url, texto_email, relatorio_nome, copia_email, unidade_email):

    # #Abrindo o Navegador
    navegador = webdriver.Chrome(ChromeDriverManager().install())

    time.sleep(5)

    #Abrindo o Pronto
    navegador.get("http://correio.blumenau.sc.gov.br/")

    time.sleep(1)

    email = navegador.find_element(By.XPATH, '//*[@id="content"]/main/form/div/div/section[2]/label/input')
    email.click()
    email.send_keys("gabrielprimo@blumenau.sc.gov.br")

    time.sleep(1)

    proximo = '//*[@id="content"]/main/form/div/div/section[3]/div/button'
    proximo = navegador.find_element(By.XPATH, proximo)
    proximo.click()

    time.sleep(1)

    senha = '//*[@id="content"]/main/form/div/div/section[3]/label/input'
    senha = navegador.find_element(By.XPATH, senha)
    senha.send_keys('sS112358')

    time.sleep(1)

    proximo = '//*[@id="content"]/main/form/div/div/section[4]/div/button'
    proximo = navegador.find_element(By.XPATH, proximo)
    proximo.click()

    time.sleep(2)

    # botão de criar email
    enviar = '//*[@id="gui.frm_main.hmenu1/0"]/span'
    enviar = navegador.find_element(By.XPATH, enviar)
    enviar.click()

    time.sleep(0.5)

    # Destinatário de E-mail
    navegador.switch_to.default_content()
    para = '//*[@id="gui.frm_compose.to.plus#main"]'
    para = navegador.find_element(By.XPATH, para)
    para.click()
    para.send_keys(unidade_email)
    para.send_keys(Keys.TAB)


    # Cópia do Email
    copia = '//*[@id="gui.frm_compose.cc.plus#main"]'
    copia = navegador.find_element(By.XPATH, copia)
    copia.click()
    copia.send_keys(copia_email)
    copia.send_keys(Keys.TAB)

    # Assunto do E-mail
    time.sleep(0.5)
    assunto = '//*[@id="gui.frm_compose.subject#main"]'
    assunto = navegador.find_element(By.XPATH, assunto)
    assunto.click()
    assunto.send_keys(relatorio_nome)
    assunto.send_keys(Keys.TAB)

    # Corpo do E-mail
    time.sleep(0.5)
    navegador.switch_to.frame(0)
    corpo_email = navegador.switch_to.active_element
    corpo_email.send_keys(texto_email)
    corpo_email.send_keys(url)
    navegador.switch_to.default_content()

    #     Botão de Enviar
    time.sleep(1)
    enter = '//*[@id="gui.frm_compose.x_btn_send#main"]'
    enter = navegador.find_element(By.XPATH, enter)
    enter.click()

    time.sleep(10)

    navegador.close()
