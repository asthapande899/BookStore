from books.models import Book

Book.objects.create(
    title="Python for Beginners",
    author="John Doe",
    price=29.99,
    description="Learn Python programming from scratch"
)

Book.objects.create(
    title="Django Web Development",
    author="Jane Smith",
    price=39.99,
    description="Build websites with Django"
)