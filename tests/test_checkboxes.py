from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_checkboxes(driver):
    driver.get(f"{BASE_URL}/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
    
    # Verificar el estado inicial de los checkboxes
    assert not checkboxes[0].is_selected()  # El primer checkbox no está seleccionado
    assert checkboxes[1].is_selected()       # El segundo checkbox está seleccionado
    
    # Cambiar el estado de los checkboxes
    checkboxes[0].click()  # Seleccionar el primer checkbox
    checkboxes[1].click()  # Deseleccionar el segundo checkbox
    
    # Verificar el nuevo estado de los checkboxes
    assert checkboxes[0].is_selected()  # El primer checkbox ahora está seleccionado
    assert not checkboxes[1].is_selected()  # El segundo checkbox ahora no está seleccionado