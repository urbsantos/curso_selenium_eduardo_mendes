from selenium.webdriver import Chrome

url = 'https://curso-python-selenium.netlify.app/aula_05_c.html'

chrome = Chrome(executable_path=r'./drivers/chromedriver.exe')

chrome.get(url)

def melhor_filme(browser, filme, email, telefone):
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme(chrome, 
            'Parasita', 
            'urbanolopes@gmail.com', 
            '(081)985198850'
            )
