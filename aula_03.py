from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Chrome(executable_path=r'./drivers/chromedriver.exe')

navegador.get(url)
sleep(1)

a = navegador.find_element_by_tag_name('a')

for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do último p: {ps[-1].text} valor do click: {click}')

    print(f'Os valores são iguais {ps[-1].text == str(click)}')


print(f'texto de a: {a.text}')

navegador.quit()
