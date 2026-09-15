import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from datetime import date

from library.models import Author, AuthorProfile, Book, Category, Publication, Publisher

print('=' * 60)
print('PRUEBA DE BORRADO on_delete=CASCADE')
print('=' * 60)

# 1) AuthorProfile -> Author (OneToOneField, CASCADE)
a = Author.objects.create(name='Autor Temporal', nationality='X')
a_id = a.pk
AuthorProfile.objects.create(author=a, bio='Perfil temporal')
print('1) OneToOneField CASCADE (Author -> AuthorProfile)')
print(f'   autor creado: {a.name}')
print(f'   perfiles antes: {AuthorProfile.objects.filter(author_id=a_id).count()}')
a.delete()
print(f'   autor borrado -> perfiles restantes: {AuthorProfile.objects.filter(author_id=a_id).count()}')
print()

# 2) Publication -> Book (ForeignKey, CASCADE)
author2 = Author.objects.create(name='Autor Temporal 2', nationality='X')
book = Book.objects.create(title='Libro Temporal', author=author2)
publisher = Publisher.objects.create(name='Editorial Temporal')
cat = Category.objects.create(name='Categoria Temporal')
cat_id = cat.pk
book.categories.add(cat)
Publication.objects.create(book=book, publisher=publisher, date=date(2000, 1, 1), edition='1a edicion')
print('2) ForeignKey CASCADE (Book -> Publication)')
print(f'   publicaciones antes: {Publication.objects.filter(book=book).count()}')
book_id = book.pk
book.delete()
print(f'   libro borrado -> publicaciones restantes: {Publication.objects.filter(book_id=book_id).count()}')
print(f'   categoria sigue existiendo (el M2M solo quita el enlace): {Category.objects.filter(pk=cat_id).exists()}')

# Limpieza de objetos temporales restantes
author2.delete()
publisher.delete()
cat.delete()
print()
print('Limpieza de objetos temporales completada.')
