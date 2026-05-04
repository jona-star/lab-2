from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    return chrome_options

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    """CASO 1: Login Exitoso"""
    print("Ejecutando Caso 1: Login...")
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url
    print("✅ Caso 1 completado con éxito.")

def test_agregar_al_carrito(driver):
    """CASO 2: Agregar al Carrito"""
    print("Ejecutando Caso 2: Agregar producto...")
    if "inventory.html" not in driver.current_url:
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_carrito == "1"
    print("✅ Caso 2 completado con éxito.")

def test_login_fallido():
    """CASO 3: Login Fallido - usa su propio driver limpio"""
    print("Ejecutando Caso 3: Login fallido...")

    # Driver completamente nuevo, sin estado previo
    driver3 = webdriver.Chrome(options=get_chrome_options())
    wait = WebDriverWait(driver3, 15)

    try:
        driver3.get("https://www.saucedemo.com")

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        error_msg = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Sorry, this user has been locked out" in error_msg.text
        print("✅ Caso 3 completado con éxito.")

    finally:
        driver3.quit()  # Siempre cerrar aunque falle