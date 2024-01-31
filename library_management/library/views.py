from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User, Book, BookDetails,BorrowedBooks
from .serializers import UserSerializer,BookSerializer, BookDetailsSerializer,BorrowedBooksSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListAllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserByIDView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'UserID'


class AddNewBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListAllBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GetBookByIDView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookID'

class AssignUpdateBookDetailsView(generics.UpdateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'BookID'

class BorrowBookView(generics.CreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class ReturnBookView(generics.UpdateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class ListAllBorrowedBooksView(generics.ListAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
