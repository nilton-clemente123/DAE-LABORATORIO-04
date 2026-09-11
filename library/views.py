from django.shortcuts import get_object_or_404, render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})
