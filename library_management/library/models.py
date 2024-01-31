from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name
    

# library/models.py
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
    

# library/models.py
class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

    def __str__(self):
        return f"Details for {self.BookID.Title}"
    

# library/models.py
class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField(auto_now_add=True)
    ReturnDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.User.Name} borrowed {self.Book.Title}"