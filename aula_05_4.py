from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://curso-python-selenium.netlify.app/aula_05.html'

chrome = Chrome(executable_path=r'./drivers/chromedriver.exe')

chrome.get(url)

campo_nome = '//input[@id="nome"]'
campo_email = '//input[@id="email"]'
campo_senha = '//input[@id="senha"]'
campo_telefone = '//input[@id="telefone"]'
botao_enviar = '//input[@id="btn"]'

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_xpath(campo_nome).send_keys(nome)
    browser.find_element_by_xpath(campo_email).send_keys(email)
    browser.find_element_by_xpath(campo_senha).send_keys(senha)
    browser.find_element_by_xpath(campo_telefone).send_keys(telefone)
    browser.find_element_by_xpath(botao_enviar).click()

sleep(2)

estrutura = {
    'nome': 'Urbano',
    'email': 'urbanolopes@gmail.com',
    'senha': 'abcde12345',
    'telefone': '81985198850'
}

preenche_form(chrome,**estrutura)

url_parseada = urlparse(chrome.current_url)

sleep(2)

texto_resultado = chrome.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_resultado = loads(resultado_arrumado)

assert dic_resultado == estrutura

chrome.quit()
