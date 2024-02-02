## Library API Development using the Django REST Framework

Create a virtualenv ```python3 -m venv env```

run command ```pip install requirements.txt```

Add Django REST Framework using ```pip install djangorestframework```

You have to notify django of the new installation in django_project/settings.py

in the INSTALLED_APPS section add rest_framework,library app

``` settings.py
   "rest_framework",
    libraryapp
```



## Serelizers

A ```Serializer``` translates complex data like querysets and model instances into a format that is easy to consume over the internet, typically JSON. It is also possible to “deserialize” data, literally the same process in reverse, whereby JSON data is first validated and then transformed into a dictionary.

The real beauty of Django REST Framework lies in its serializers which abstracts away most of the complexity for us. We will cover serialization and JSON in more depth in future chapters but for now the goal is to demonstrate how easy it is to create a serializer with Django REST Framework.


##run server
```(.venv) > python manage.py runserver```

location of our API endpoint is at ```http://127.0.0.1:8000/api/``` so navigate there in your web browser


Update your Django project settings (library_management/settings.py) to use MySQL as the database. Replace the DATABASES section with the following:

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # Set to your MySQL server's host (usually 'localhost' for local development)
        'PORT': '3306',       # Set to your MySQL server's port (usually '3306' for default MySQL installations)
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

```
# With these models, you have established the specified attributes and relationships:

1-M relationship between User and BorrowedBooks.
1-1 relationship between Book and BookDetails.
1-M relationship between User and BorrowedBooks.

## Create MySQL Database

```mysql -u your_mysql_username -p```

```CREATE DATABASE your_database_name;```

# Apply migrations
```python manage.py makemigrations
python manage.py migrate
```

## Token Authentication 
In settings.py
```REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

# Get Token for your superuser username
```python manage.py drf_create_token <your_username>```
# Retrieve Token

```Generated token for user 'your_username': 0123456789abcdef0123456789abcdef01234567```


# Create User:
```curl -X POST -H "Content-Type: application/json" -d '{"Name": "John Doe", "Email": "john@example.com", "password": "your_password"}' http://localhost:8000/api/users/create/ ```

# List All Users:
```curl -X GET -H "Authorization: Token YOUR_TOKEN_HERE" http://localhost:8000/api/users/```

# Get User by ID:
```curl -X GET -H "Authorization: Token YOUR_TOKEN_HERE" http://localhost:8000/api/users/1/```

# Add New Book:
```curl -X POST -H "Content-Type: application/json" -H "Authorization: Token YOUR_TOKEN_HERE" -d '{"Title": "Sample Book", "ISBN": "1234567890", "PublishedDate": "2022-01-30", "Genre": "Fiction"}' http://localhost:8000/api/books/create/```

# Get book by id
```curl -X GET -H "Authorization: Token YOUR_TOKEN_HERE" http://localhost:8000/api/books/1/```
# List All Borrowed Books:
```curl -X GET -H "Authorization: Token YOUR_TOKEN_HERE" http://localhost:8000/api/borrowed_books/```


# You can use other urls to available in same ways

