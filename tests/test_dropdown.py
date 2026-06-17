from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_seleccionar_dropdown(driver):
    driver.get(f"{BASE_URL}/dropdown")
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text("Option 2")
    assert select.first_selected_option.text == "Option 2"

