from rest_framework import serializers
from recipes.models import Recipe, Review
from django.contrib.auth.models import User
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'category', 'ingredients', 'cuisine']
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    def create(self, validated_data):
        u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        u.save()
        return u
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review', 'rating', 'recipe', 'user']