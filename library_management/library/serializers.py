
from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'