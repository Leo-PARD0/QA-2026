# importar o selenium webdriver
from selenium import webdriver

# importar Options() para configurar o navegador
from selenium.webdriver.chrome.options import Options

# importar By para selecionar coisas nos sites
from selenium.webdriver.common.by import By

# importar keys para passar comandos para o navegador
from selenium.webdriver.common.keys import Keys

# importar expect condition para informar o resultado esperado
from selenium.webdriver.support import expected_conditions as EC

# importar webdriverwait para esperar
from selenium.webdriver.support.ui import WebDriverWait

# importar time para pedir para esperar
import time

# configurar o navegador
options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com')

time.sleep(10)

print('Escaneie o código QR com seu celular!')
wait = WebDriverWait(driver, 60)

# precisamos selecionar a caixa de pesquisa
# WAIT.UNTIL serve para verificar se o elemento está presente
caixa_pesquisa = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div[1]/div/div/div/div/div'))
)

time.sleep(2)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
time.sleep(1)

# os dados
grupo = "QA 2026 IBTECH Alunos"

texto = 'LEONARDO: Esta mensagem é automática e foi enviada com selenium'

caixa_pesquisa.click()
caixa_pesquisa.send_keys(grupo)

time.sleep(2)

campo_mensagem = driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')

campo_mensagem.click()
campo_mensagem.send_keys(texto)
campo_mensagem.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()