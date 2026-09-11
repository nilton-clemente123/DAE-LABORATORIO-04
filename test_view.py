import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from library.models import Book

c = Client(SERVER_NAME='localhost')
b = Book.objects.get(title='Cien años de soledad')
r = c.get(f'/book/{b.pk}/')
print('Status:', r.status_code)
if r.status_code == 200:
    print(r.content.decode())
else:
    print('--- CONTENIDO (primeras lineas) ---')
    text = r.content.decode()
    print(text[:2000])