from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Perfil de autor'
        verbose_name_plural = 'Perfiles de autores'

    def __str__(self):
        return f'Perfil de {self.author.name}'


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='libros',
    )
    categories = models.ManyToManyField(Category, related_name='libros')
    publishers = models.ManyToManyField(
        Publisher,
        through='Publication',
        related_name='libros',
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title


class Publication(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date = models.DateField()
    edition = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f'{self.book.title} - {self.publisher.name}'