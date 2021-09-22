# comandos

# iniciar entorno virtual 
python3 -m venv rest_framework
# Activar entorno 
source rest_framework/bin/activate
# SAlir del entorno 
desactivate

# instalar paquetes desde un txt
pip install -r requierements.txt

# iniciar proyecto 
django-admin atartproject profile_project .

# Iniciar app
python3 manage.py startapp profiles_api

# migraciones de toda la app
python manage.py migrate
# Migracion de un archivo 
python manage.py makemigrations profiles_api

# Crear super usuario 
python manage.py createsuperuser

# Ejecutar el servidor
python manage.py runserver