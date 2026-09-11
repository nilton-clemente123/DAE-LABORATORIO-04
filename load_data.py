import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from library.models import Author, AuthorProfile, Book, Category, Publication, Publisher

# Autores
a1 = Author.objects.create(
    name='Gabriel García Márquez',
    birth_date=date(1927, 3, 6),
    nationality='Colombiana',
)
a2 = Author.objects.create(
    name='Mario Vargas Llosa',
    birth_date=date(1936, 3, 28),
    nationality='Peruana',
)

# Perfiles de autor
AuthorProfile.objects.create(
    author=a1,
    bio='Premio Nobel de Literatura 1982.',
    website='https://example.com/ggm',
)
AuthorProfile.objects.create(
    author=a2,
    bio='Premio Nobel de Literatura 2010.',
    website='https://example.com/mvl',
)

# Categorías
c1 = Category.objects.create(name='Novela', description='Obras de ficción narrativa')
c2 = Category.objects.create(name='Realismo mágico', description='Género literario latinoamericano')
c3 = Category.objects.create(name='Ensayo', description='Textos de reflexión y análisis')

# Editoriales
p1 = Publisher.objects.create(
    name='Editorial Sudamericana',
    address='Buenos Aires, Argentina',
    website='https://example.com/sudamericana',
)
p2 = Publisher.objects.create(
    name='Alfaguara',
    address='Madrid, España',
    website='https://example.com/alfaguara',
)

# Libros
b1 = Book.objects.create(
    title='Cien años de soledad',
    isbn='978-0307474728',
    publication_date=date(1967, 5, 30),
    author=a1,
)
b1.categories.add(c1, c2)  # libro en dos categorías

b2 = Book.objects.create(
    title='El amor en los tiempos del cólera',
    isbn='978-0307389732',
    publication_date=date(1985, 1, 1),
    author=a1,
)
b2.categories.add(c1)

b3 = Book.objects.create(
    title='La ciudad y los perros',
    isbn='978-0060882860',
    publication_date=date(1963, 1, 1),
    author=a2,
)
b3.categories.add(c1)

b4 = Book.objects.create(
    title='La casa verde',
    isbn='978-0060732806',
    publication_date=date(1966, 1, 1),
    author=a2,
)
b4.categories.add(c1, c2)  # libro en dos categorías

# Publicaciones (modelo intermedio Book <-> Publisher)
Publication.objects.create(book=b1, publisher=p1, date=date(1967, 5, 30), edition='1ª edición')
Publication.objects.create(book=b2, publisher=p2, date=date(1985, 1, 1), edition='1ª edición')
Publication.objects.create(book=b3, publisher=p1, date=date(1963, 1, 1), edition='1ª edición')
Publication.objects.create(book=b4, publisher=p2, date=date(1966, 1, 1), edition='1ª edición')

print('Datos de prueba cargados correctamente.')