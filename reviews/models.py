from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    photo = models.ImageField(blank=True, upload_to='product_images/')
    product_id = models.CharField(max_length=50)


class Review(models.Model):
    title = models.CharField(max_length=20)
    score = models.IntegerField()
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='review_images/')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    created_at = models.DateTimeField(auto_now_add=True)