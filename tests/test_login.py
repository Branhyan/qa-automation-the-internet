from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_login_exitoso(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in flash


def test_login_password_fail(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperIncorrectPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in flash


def test_login_username_fail(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys("usuarioincorrecto")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in flash

