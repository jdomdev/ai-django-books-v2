from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
# List of all books
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})
# Detail of a book 
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})
# Create a new book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'books/book_create.html', {'form': form})
# Update a book
def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form, 'book': book})
# Delete a book
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'books/book_delete.html', {'book': book})