from django.urls import path
from .import views


urlpatterns = [
    path('books', views.Books.as_view(), name='books'),
    path('book/<int:id>', views.BookById.as_view(), name='book'),
    path('add_book', views.AddBook.as_view(), name='add_book'),
    path('update_book/<int:id>', views.UpdateBook.as_view(), name='update_book'),
    path('delete_book/<int:id>', views.DeleteBook.as_view(), name='update_book'),
]