from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import os

# Configuración inicial
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Inicializar el driver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

def ejecutar_pruebas_robustas():
    try:
        # --- CASO 1: Login Exitoso con Esperas Explícitas ---
        print("Ejecutando Caso 1: Login con esperas explícitas...")
        driver.get("https://saucedemo.com")
        
        # Esperar a que el campo de usuario sea visible
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")
        
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("secret_sauce")
        
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
        # Esperar a que la URL cambie
        wait.until(EC.url_contains("inventory.html"))
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al Carrito con Esperas ---
        print("Ejecutando Caso 2: Agregar producto con esperas...")
        boton_agregar = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        boton_agregar.click()
        
        badge_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge_carrito.text == "1"
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login Fallido con Esperas ---
        print("Ejecutando Caso 3: Login fallido con esperas...")
        driver.delete_all_cookies()
        driver.get("https://saucedemo.com")
        
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("locked_out_user")
        
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("secret_sauce")
        
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
        # Esperar a que aparezca el mensaje de error
        error_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert "Sorry, this user has been locked out" in error_msg.text
        print("✅ Caso 3 completado con éxito.")

    except TimeoutException as te:
        print(f"❌ Timeout: El elemento no se encontró en el tiempo esperado - {te}")
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas_robustas()
