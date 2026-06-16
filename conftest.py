import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # gestiona el proceso del chromedriver (el ejecutable que conecta Selenium con Chrome)
from webdriver_manager.chrome import ChromeDriverManager # es como "el instalador" de chromedriver

BASE_URL = "https://the-internet.herokuapp.com"

@pytest.fixture #Los fixtures son como funciones para "envolver" los test conectando y desconectando el driver
def driver():
    options = webdriver.ChromeOptions() #options es como para configurar el entorno de el navegador.
    # options.add_argument("--headless=new")
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options 
    )
    drv.implicitly_wait(5)
    yield drv #arriba = setup, abajo = teardown o sea, arriba se prepara para el test, abajo se cierra el entorno de pruebas
    drv.quit()

