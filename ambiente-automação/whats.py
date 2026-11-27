# importar o webdriver do selenium
from selenium import webdriver
# importar Options() para configurar o navegador
from selenium.webdriver.chrome.options import Options
# importar By() para selecionar coisas no site
from selenium.webdriver.common.by import By
# importar Keys() para mandar comandos para o navegador
from selenium.webdriver.common.keys import Keys
# importar WebDriverWait para mandar o navegador esperar
from selenium.webdriver.support.ui import WebDriverWait
# importar expected conditions para informar qual é o resultado esperado
from selenium.webdriver.support import expected_conditions as EC

# import time para esperar
import time

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com')

time.sleep(10)

mensagem = 'LEONARDO: esta mensagem foi enviada automaticamente'
grupo = 'QA 2026 IBTECH Alunos'

print('Escaneie o código QR com seu celular!')
wait = WebDriverWait(driver, 60)

# encontrar caixa de pesquisa
caixa_pesquisa = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div/div[2]/input')))

time.sleep(2)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
time.sleep(1)

caixa_pesquisa.click()
caixa_pesquisa.send_keys(grupo)
time.sleep(1)
caixa_pesquisa.send_keys(Keys.ENTER)

time.sleep(1)

campo_mensagem = driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')

campo_mensagem.send_keys(mensagem)
time.sleep(1)
caixa_pesquisa.send_keys(Keys.ENTER)


input()