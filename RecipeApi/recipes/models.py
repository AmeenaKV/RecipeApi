from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Review(models.Model):
    review = models.CharField(max_length=30)
    rating = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    def __str__(self):
        return self.recipe.name