from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    #return render(request, 'books/books_list.html', {'books': books})


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    # Before we can perform any operations on a book, 
    # we need to check if the book exists
    try:
        book_for_id = Book.objects.get(pk=book_id)
    except book_for_id.DoesNotExist:  # Corregido: Usar Book.DoesNotExist
        return Response({"error": "El libro que busca no se ha encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book_for_id)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Corregido: Pasar la instancia del libro para actualizarla
        serializer = BookSerializer(book_for_id, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda los cambios en la instancia del libro
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Corregido: Devolver errores si el serializador no es válido
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        book_for_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def book_create(request):
    data = request.data
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

""" @api_view(['UPDATE'])
def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form, 'book': book}) """

""" @api_view(['DELETE'])
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'books/book_delete.html', {'book': book}) """