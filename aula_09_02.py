from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


def esperar_botao(webdriver):
    elements = webdriver.find_elements_by_css_selector('button')
    print('Tentando encontrar o "button"')
    return bool(elements) # Se a lista estiver vazia -> False, caso contrário -> True


def esperar_sucesso(webdriver):
    elements = webdriver.find_elements_by_css_selector('#finished')
    print('Tentando encontrar a "mensagem de sucesso"')
    return bool(elements) # Se a lista estiver vazia -> False, caso contrário -> True

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
