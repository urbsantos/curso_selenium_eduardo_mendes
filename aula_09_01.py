from selenium.webdriver import Chrome

url = 'https://curso-python-selenium.netlify.app/aula_09_a.html'

browser = Chrome(executable_path=r'./drivers/chromedriver.exe')

browser.get(url)
browser.implicitly_wait(30)

btn = browser.find_elements_by_css_selector('button')
btn.click()

sucesso = browser.find_elements_by_css_selector('#finished')
assert sucesso.text == 'Carregamento concluido'
