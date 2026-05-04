# Automatización de Pruebas Funcionales con Selenium

Proyecto de automatización de pruebas para la tienda virtual **Sauce Demo** utilizando Python y Selenium.

## 📋 Casos de Prueba

| ID | Caso de Uso | Descripción | Resultado Esperado |
|----|-------------|-------------|-------------------|
| 01 | Login Exitoso | Ingresar credenciales válidas | El usuario llega al dashboard de productos |
| 02 | Agregar al Carrito | Hacer clic en "Add to cart" | El icono del carrito muestra el número "1" |
| 03 | Login Fallido | Ingresar un usuario bloqueado | Aparece un mensaje de error en pantalla |

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- Google Chrome instalado
- pip (gestor de paquetes de Python)

### Instalar Dependencias

**Opción 1: Instalación automática (Recomendada)**
```bash
pip install -r requirements.txt
```

**Opción 2: Si tienes problemas con ChromeDriver**

Selenium 4.6+ incluye Selenium Manager que descarga ChromeDriver automáticamente. Si aún así tienes problemas:

1. Verifica tu versión de Chrome: `chrome://version/`
2. Descarga ChromeDriver compatible desde: https://googlechromelabs.github.io/chrome-for-testing/
3. Extrae el archivo y agrégalo al PATH de Windows

### Solución de Problemas

Si ves el error "WinError 193", ejecuta:
```bash
pip install selenium --upgrade
```

## ▶️ Ejecución

### Script Básico
```bash
python test_practico.py
```

### Script con Esperas Explícitas (Recomendado)
```bash
python robust_test.py
```

### Ejecutar desde VS Code
1. Abre cualquier archivo `.py`
2. Haz clic en el botón ▶️ (Run Python File) en la esquina superior derecha
3. O presiona `F5` para ejecutar con el debugger

## 🏗️ Estructura del Proyecto

```
selenium-saucedemo/
├── test_practico.py
├── robust_test.py
├── requirements.txt
└── README.md
```

## 🔧 Tecnologías

- **Selenium WebDriver 4.16** - Automatización del navegador
- **Python 3.x** - Lenguaje de programación
- **WebDriver Manager** - Gestión automática de ChromeDriver
- **Explicit Waits** - Manejo robusto de sincronización

## 📝 Notas

- URL de pruebas: https://saucedemo.com
- Usuario válido: `standard_user`
- Usuario bloqueado: `locked_out_user`
- Contraseña: `secret_sauce`
