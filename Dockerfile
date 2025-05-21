# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo los archivos de requerimientos para aprovechar cache
COPY requirements.txt /app/

# Instala dependencias
RUN pip install --upgrade pip && pip install -r  requirements.txt


# Copia todo el proyecto dentro del contenedor
COPY . /app/

# Expone el puerto 8000 para el servidor Django
EXPOSE 8000

# Comando para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
