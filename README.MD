# Proyecto Librería
## Proyecto realizado con Django para la gestión de una librería

## Advertencias

> **Advertencia:** Este proyecto es solo para fines educativos. No se recomienda su uso en producción.

⚠️ **Asegúrate de tener todas las dependencias y requerimientos instalados antes de ejecutar el proyecto.**

---
## Instalación

Para instalar el proyecto, sigue estos pasos:
1. Clona el repositorio:
    
    ```bash
    git clone https://github.com/ThePowerty/libreria.git
    ```

2. Creamos el entorno virtual:
    
    ```bash
    python3 -m venv env
    ```

3. Activamos el entorno virtual:
    
    ```bash
    source env/bin/activate
    ```

4. Instalamos las dependencias
    
    ```bash
    pip3 install -r requirements.txt
    ```

5. Añadimos datos de prueba
    ```bash
    python manage.p shell < create_data.py
    ```
---
# Requisitos

Antes de ejecutar el proyecto, asegúrate de tener un archivo `.env` configurado. Este archivo contiene variables de entorno necesarias para el funcionamiento del apartado de *contacto*.

## Configuración del archivo .env

1. Copia el archivo de ejemplo:
   
   ```bash
   cp .env.example .env
   ```

2. Editar y añadir tus credenciales a las variables de entorno

> **Advertencia:** Para el uso del apartado de *contacto* con Gmail es necesario tener una clave aplicación para añadirla a las variables de entorno.

> Para usar el apartado de *contacto* a traves de una configuración de un servidor smtp propio es necesario editar el apartado de `Configuración de correo` del archivo *settings*.
---
## 📝Credenciales

A continuación se presentan la creación de un super usuario para el inicio de sesión como administrador. 

```bash
python manage.py createsuperuser --username=admin --email=admin@example.com
```
Por razones de seguridad Django no permite establecer la contraseña como un parámetro por ello debe ser ingresada de forma interactiva.

**Recomendación**:
- **Nombre de usuario**: `admin`
- **Email de usuario**: `admin@example.com`
- **Contraseña**: `admin123.`

🚨 **Estas credenciales son solo para fines de demostración y no deben usarse en un entorno de producción.**