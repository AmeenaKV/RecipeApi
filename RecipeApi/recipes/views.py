from django.shortcuts import render
from recipes.models import Recipe, Review
from recipes.serializers import RecipeSerializer, ReviewSerializer, UserSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.
class CreateListRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
class EditDeleteRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
# class SearchRecipe(APIView):
#     def get(self, request):
#         query = self.request.query_params.get('SearchRecipe')
#         if query:
#             recipes = Recipe.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
#             r = RecipeSerializer(recipes, many=True)
#             return Response(r.data)
class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class CreateListReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
class ViewReview(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SearchRecipe(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category', 'ingredients', 'cuisine']