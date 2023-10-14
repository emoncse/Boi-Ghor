from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    language = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField()
    similar_books = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review for {self.book.name} by {self.reviewer_name}"
