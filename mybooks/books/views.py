from django.shortcuts import render, get_object_or_404
from .models import Book

def detail(request, id):
  book = get_object_or_404(Book, id=id)
  return render(request, "detail.html", {'book': book})


def index(request):
  books = Book.objects.all()
  return render(request, "index.html", {'books': books})
