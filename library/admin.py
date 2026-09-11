from django.contrib import admin

from .models import Author, AuthorProfile, Book, Category, Publication, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'nationality')


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('author', 'website')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date')
    filter_horizontal = ('categories',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('book', 'publisher', 'date', 'edition')