
# API REST TYBATEST

Esta es una API REST desarrollada con Django REST Framework cumplir con la prueba tecnica Tyba Backend Engineer.

---
## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Documentación de la API](#documentación-de-la-api)

---

## Descripción

API REST que permita: 
    1.  Registro de usuario.
    2.  Login de usuario.
    3.  Crear un endpoint para los usuarios logueados el cual reciba
        una ciudad (o unas coordenadas) y retorne una lista de los
        restaurantes cercanos a esta ciudad o coordenadas. Puedes
        utilizar algún API público para esto.
    4.  Crear un endpoint donde puedes consultar la lista de las
        transacciones realizadas históricamente.
    5.  Logout de usuario.
    6.  Correr localmente desde docker con docker-compose.

---

## Características

- Listar restaurantes 
- Buscar restaurantes
- Generar login
- Autenticar usuarios
- Documentación automática con Swagger (drf-yasg)
- Validación y serialización de datos
- Visualizar logs

---

## Instalación

Clona este repositorio:

```bash
git clone https://github.com/cabetto103/tybaTest.git
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Ejecuta las migraciones:

```bash
python manage.py migrate
```

Crea un superusuario (opcional):

```bash
python manage.py createsuperuser
```
---
## Uso

Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

La API estará disponible en:

```
http://localhost:8000/api/usuarios/registro/
http://localhost:8000/api/usuarios/login/
http://localhost:8000/api/funciones/consultar_restaurantes/?ciudad="nombre_ciudad"
http://localhost:8000/api/funciones/consultar_restaurantes/?latitud=4.6097&longitud=-74.0817
http://localhost:8000/api/logs/logs_consultas_restaurantes/
http://localhost:8000/api/usuarios/logout/

---

## Documentación de la API

La documentación automática de la API está disponible en Swagger UI:

```
http://localhost:8000/swagger/
```

Allí podrás ver los endpoints, descripciones, y probar la API desde el navegador.

---