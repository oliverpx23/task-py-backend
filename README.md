## README

**Requisitos previos**

* Python 3.11

**Configuración del entorno**

1. Crear un entorno virtual con venv:

```bash
python3 -m venv .venv
```

2. Activar el entorno virtual:

```bash
source .venv/bin/activate
```

**Instalación de dependencias**

1. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

**Configuración de variables de entorno**

1. Crear un archivo `.env` con las variables de entorno según el archivo `.env.template`.

2. La propiedad `DB_URL` es la URL de conexión a la base de datos.

3. Si no se proporciona `DB_URL`, se crea una base de datos SQLite3 por defecto.

**Migración de datos a la base de datos**

1. Ejecutar el comando para migrar los datos a la base de datos:

```bash
python manage.py migrate
```

**Compilación de la aplicación y archivos estáticos**

1. Compilar los archivos estáticos para la aplicación:

```bash
python manage.py collectstatic
```

**Ejecución de la aplicación en modo desarrollo**

1. Iniciar el servidor de desarrollo para ejecutar la aplicación:

```bash
python manage.py runserver
```

**Despliegue automático**

1. Al realizar un push a la rama `main`, se ejecutará el proceso de CI/CD a partir del archivo `Procfile` en la plataforma Railway.
