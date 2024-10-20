# Usa una imagen base de Python 3.9 ligera
FROM python:3.9-slim

# Instala git para clonar repositorios si es necesario
RUN apt-get update && apt-get install -y git

# Establece el directorio de trabajo a /app
WORKDIR /app

# Clona el repositorio de GitHub donde está el proyecto
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Malena2317.git

# Cambia el directorio de trabajo al repositorio clonado
WORKDIR /app/ajedrez-2024-Malena2317

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar pruebas unitarias con cobertura y luego iniciar la aplicación
CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python Cli.py"]
