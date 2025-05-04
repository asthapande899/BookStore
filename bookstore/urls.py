from django.contrib import admin
from django.urls import path  # THIS IMPORT IS MISSING
from books.views import welcome, book_list, add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('books/', book_list, name='book_list'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]