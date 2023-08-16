# Django Image Upload with Log and DB user Validation App

Esta es una aplicación Django para subir imágenes y generar registros de actividad en un servidor. La aplicación permite validar usuarios contra una base de datos Oracle y almacenar información relacionada con las imágenes subidas.

## Características

- Subida de imágenes en formato PNG o JPG.
- Validación de tamaño y formato de imagen.
- Validación de usuarios contra una base de datos Oracle.
- Generación de registros de actividad en archivos de registro diarios.
- Integración con la API REST de Django.

## Instalación

1. Clona este repositorio a tu máquina local:

   ```bash
   git clone https://github.com/nicoriver9/Django-ImageUpload-Log-DB-UserValidation.git
   cd YOUR_REPOSITORY

2. Crea un entorno virtual y actívalo:

        python -m venv venv
        source venv/bin/activate
3. Instala dependencias:
        
        pip install -r requirements.txt

4. Ejecuta las migraciones de la base de datos:

        python manage.py migrate

## Uso

1. Inicia el servidor de desarrollo: 

        python manage.py runserver


2. Accede a la aplicación en tu navegador: http://localhost:8000
3. Utiliza herramientas como Postman para interactuar con la API de subida de imágenes.        

## Estructura del Proyecto

* image_storage_api/ : Directorio principal de la aplicación Django.
    * images/ : App de Django para subir imágenes y generar registros.
    * media/ : Directorio donde se almacenan las imágenes subidas.
    * logs/ : Directorio donde se almacenan los archivos de registro diarios.
* frontend/ : Directorio para la parte frontend de la aplicación (React, opcional).

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras errores o tienes mejoras, no dudes en crear un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.
