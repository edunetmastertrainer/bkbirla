# Django Rest Framework

1. pip install django
2. pip install djangorestframework
3. django-admin startproject library
4. cd library
5. python manage.py startapp books
6. Open library/settings.py in a text editor.
       - INSTALLED_APPS = [
          # ... existing apps ...
          'rest_framework',
          'books',
      ]
7. define books/models.py
8. Create a new file books/serializers.py
9. books/views.py
    -  class BookListCreateView,
    -  class BookDetailView(generics.RetrieveUpdateDestroyAPIView)
10. books/urls.py
      - path('books/', BookListCreateView.as_view(), name='book-list-create'),
      - path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
11. python manage.py makemigrations
12. python manage.py migrate
13. python manage.py runserver
14. Update a Book by ID - add   "lookup_field = 'id'" in view.py
15. pip install django-cors-headers
16.add 'corsheaders' to INSTALLED_APPS, and add CORS_ALLOWED_ORIGINS = ['http://localhost:8000'] (or your frontend URL) to settings.py.
17. add this in seeting.py - >  'corsheaders.middleware.CorsMiddleware'
