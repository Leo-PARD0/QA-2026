# importar o selenium webdriver
from selenium import webdriver

# importar Options() para configurar o navegador
from selenium.webdriver.chrome.options import Options

# importar By para selecionar coisas nos sites
from selenium.webdriver.common.by import By

# importar keys para passar comandos para o navegador
from selenium.webdriver.common.keys import Keys

# importar time para pedir para esperar

# configurar o navegador
options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://www.jogajuntoinstituto.org/')

input()