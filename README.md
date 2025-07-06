# Drive and Deal 🏎️
Aplicación web desarrollada con **FastAPI**, **MongoDB Atlas** y **Jinja2** para la gestión integral de una empresa de renta de autos. Este sistema permite a distintos roles (empleados, encargados y dueño) realizar operaciones clave como el registro de clientes, administración de vehículos, gestión de rentas y devoluciones, así como el seguimiento de reparaciones y consultas de autos más rentados.

# Instalación ⚙️
### 1. Clonar el repositorio
```

git clone https://github.com/slaughtbear/Drive-and-Deal-App.git

```

### 2. Crear un entorno virtual
```

python -m venv venv

```

### 3. Activar el entorno virtual
#### Linux/MacOS
```

source venv/bin/activate

```

#### Windows
```

venv\Scripts\activate

```

### 4. Instalar las dependencias
```

pip install -r requirements.txt

```

## Dependencias del Proyecto
1. **FastAPI (0.115.14)** – Framework moderno y rápido (high-performance) para construir APIs en Python, con soporte nativo para asincronía y validación de datos mediante type hints.
2. **Motor (3.7.1)** – Cliente asíncrono para MongoDB, diseñado para trabajar eficientemente con operaciones no bloqueantes en bases de datos.
3. **Jinja2 (3.1.6)** – Motor de plantillas flexible y potente para generar HTML dinámico, integrado con FastAPI para renderizar vistas.
4. **Python Dotenv (1.1.1)** – Librería para cargar variables de entorno desde un archivo `.env`, facilitando la configuración segura y separada del código.
5. **Python Jose (3.5.0)** – Implementación de **JWT (JSON Web Tokens)** para autenticación y autorización, permitiendo el manejo seguro de tokens en APIs.
6. **Bcrypt (4.3.0)** – Algoritmo de hashing para contraseñas, proporcionando seguridad robusta mediante cifrado irreversible con salt.

## Configuración 🔧
### 1. Crear archivo `.env`
Crea en la raíz del proyecto (fuera de la carpeta src) un archivo `.env`, en el crearás todas las variables de entorno para el funcionamiento del proyecto:
- `MONGODB_URL`: Ingresa el URL de conexión que te proporciona MongoDB Atlas al momento de crear un proyecto.