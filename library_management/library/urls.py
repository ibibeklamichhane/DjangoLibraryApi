from django.urls import path
from .views import (
    CreateUserView, ListAllUsersView, GetUserByIDView,
    AddNewBookView, ListAllBooksView, GetBookByIDView, AssignUpdateBookDetailsView,
    BorrowBookView, ReturnBookView, ListAllBorrowedBooksView,
)

urlpatterns = [
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('users/', ListAllUsersView.as_view(), name='list-all-users'),
    path('users/<int:UserID>/', GetUserByIDView.as_view(), name='get-user-by-id'),

    path('books/create/', AddNewBookView.as_view(), name='add-new-book'),
    path('books/', ListAllBooksView.as_view(), name='list-all-books'),
    path('books/<int:BookID>/', GetBookByIDView.as_view(), name='get-book-by-id'),
    path('books/details/<int:BookID>/', AssignUpdateBookDetailsView.as_view(), name='assign-update-book-details'),

    path('borrowed_books/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('borrowed_books/return/', ReturnBookView.as_view(), name='return-book'),
    path('borrowed_books/', ListAllBorrowedBooksView.as_view(), name='list-all-borrowed-books'),
]
'''    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'healthapp',
        'USER': 'root',
        'PASSWORD': 'Laptop@123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}'''