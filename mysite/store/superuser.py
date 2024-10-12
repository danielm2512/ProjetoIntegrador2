import os
import django

# Configurando o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

# Criação do superusuário
if not User.objects.filter(username='meusuperuser').exists():
    User.objects.create_superuser('meusuperuser', 'camila.calado.vicente@gmail.com', '12345')
    print('Superusuário criado com sucesso!')
else:
    print('Superusuário já existe!')
