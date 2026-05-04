from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    """CASO 1: Login Exitoso"""
    print("Ejecutando Caso 1: Login...")
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url
    print("✅ Caso 1 completado con éxito.")

def test_agregar_al_carrito(driver):
    """CASO 2: Agregar al Carrito"""
    print("Ejecutando Caso 2: Agregar producto...")
    if "inventory.html" not in driver.current_url:
        driver.get("https://saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
    
    boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_carrito == "1"
    print("✅ Caso 2 completado con éxito.")

def test_login_fallido(driver):
    """CASO 3: Login Fallido (Usuario Bloqueado)"""
    print("Ejecutando Caso 3: Login fallido...")
    driver.delete_all_cookies()
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Espera explícita para que el mensaje de error aparezca
    wait = WebDriverWait(driver, 15)
    error_msg = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "Sorry, this user has been locked out" in error_msg.text
    print("✅ Caso 3 completado con éxito.")