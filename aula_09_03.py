from functools import partial
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(elemento, webdriver):
    print(f'Tentando encontrar o elemento "{elemento}"')
    if webdriver.find_elements_by_css_selector(elemento):
        return True
    return False


esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')


url = 'https://curso-python-selenium.netlify.app/aula_09_a.html'

browser = Chrome(executable_path=r'./drivers/chromedriver.exe')

wdw = WebDriverWait(browser, 10)

browser.get(url)

# Esperar o botão aparecer
wdw.until(esperar_botao, 'Não clicou no botão')

# Clicar no botão
browser.find_element_by_css_selector('button').click()

# Esperar a mensagem de sucesso
wdw.until(esperar_sucesso, 'A mensagem de sucesso não apareceu')

# Validar se a mensagem apareceu

sucesso = browser.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'

browser.quit()
