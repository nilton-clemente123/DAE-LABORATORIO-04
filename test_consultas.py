import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from library.models import Author, Book, Category, Publisher

print('=' * 60)
print('CONSULTA DE IDA (libro.author)')
print('=' * 60)
b = Book.objects.get(title='Cien años de soledad')
print(f'  libro: {b.title}')
print(f'  autor: {b.author.name}')
print()

print('=' * 60)
print('CONSULTA DE VUELTA (author.libros.all())')
print('=' * 60)
a = Author.objects.get(name='Gabriel García Márquez')
libros = a.libros.all()
print(f'  autor: {a.name}')
print(f'  libros: {[libro.title for libro in libros]}')
print()

print('=' * 60)
print('CONSULTA DE FILTRADO (doble guion bajo)')
print('=' * 60)
libros_vargas = Book.objects.filter(author__name='Mario Vargas Llosa')
print(f'  libros de Mario Vargas Llosa: {[libro.title for libro in libros_vargas]}')

libros_realismo = Book.objects.filter(categories__name='Realismo mágico')
print(f'  libros en Realismo mágico: {[libro.title for libro in libros_realismo]}')

libros_sudamericana = Book.objects.filter(publication__publisher__name='Editorial Sudamericana')
print(f'  libros de Editorial Sudamericana: {[libro.title for libro in libros_sudamericana]}')
print()

print('=' * 60)
print('CONSULTA EN SENTIDO INVERSO (categoría -> libros)')
print('=' * 60)
c = Category.objects.get(name='Realismo mágico')
print(f'  categoría: {c.name}')
print(f'  libros: {[libro.title for libro in c.libros.all()]}')
print()

print('=' * 60)
print('CONSULTA EN SENTIDO INVERSO (editorial -> libros, vía intermedio)')
print('=' * 60)
p = Publisher.objects.get(name='Editorial Sudamericana')
print(f'  editorial: {p.name}')
print(f'  libros (p.libros.all()): {[libro.title for libro in p.libros.all()]}')
print('  publicaciones (p.publication_set.all()):')
for pub in p.publication_set.all():
    print(f'    - {pub.book.title} ({pub.date} - {pub.edition})')
