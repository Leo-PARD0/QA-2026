# importar o webdriver do selenium
from selenium import webdriver
# importar Options() para configurar o navegador
from selenium.webdriver.chrome.options import Options
# importar By() para selecionar coisas no site
from selenium.webdriver.common.by import By
# importar Keys() para mandar comandos para o navegador
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://www.jogajuntoinstituto.org/')

input()