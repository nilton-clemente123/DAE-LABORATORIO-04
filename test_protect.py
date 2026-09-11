import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db.models import ProtectedError
from library.models import Author, Book

a = Author.objects.get(name='Gabriel García Márquez')
print('ANTES: libros de', a.name, '->', list(Book.objects.filter(author=a).values_list('title', flat=True)))
print('Total libros antes:', Book.objects.count())
print()
print('Intentando borrar al autor con PROTECT...')
try:
    a.delete()
    print('BORRADO EXITOSO (no deberia ocurrir)')
except ProtectedError as e:
    print('ProtectedError: no se puede borrar porque tiene libros relacionados.')
    print('Objetos protegidos:', [obj.title for obj in e.protected_objects])
print()
print('DESPUES: Total libros:', Book.objects.count())
print('Autores restantes:', list(Author.objects.values_list('name', flat=True)))