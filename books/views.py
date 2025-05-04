from django.shortcuts import render, redirect, get_object_or_404
from .models import Book  # Make sure this exists

def welcome(request):
    return render(request, 'books/welcome.html')

def book_list(request):
    books = Book.objects.all()  # This requires the Book model
    return render(request, 'books/book_list.html', {'books': books})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart', {})
    
    # Add book to cart or increase quantity
    if str(book_id) in cart:
        cart[str(book_id)]['quantity'] += 1
    else:
        cart[str(book_id)] = {
            'title': book.title,
            'price': str(book.price),
            'quantity': 1
        }
    
    request.session['cart'] = cart
    return redirect('book_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    
    # Calculate total
    total = 0
    for item in cart.values():
        total += float(item['price']) * item['quantity']
    
    return render(request, 'books/cart.html', {
        'cart': cart,
        'total': total
    })

def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        del cart[str(book_id)]
        request.session['cart'] = cart
    return redirect('view_cart')