from django.shortcuts import render  # THIS LINE IS CRUCIAL

def welcome(request):
    return render(request, 'books/welcome.html')

def book_list(request):
    books = [
        {"title": "Python for Beginners", "price": 29.99},
        {"title": "Django Web Development", "price": 39.99}
    ]
    return render(request, 'books/book_list.html', {'books': books})