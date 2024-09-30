from rest_framework import viewsets
from .models import Recipe, Ingredient, Season, Equipment, RecipeIngredient, RecipeEquipment, Cuisine
from .serializers import RecipeSerializer, IngredientSerializer, SeasonSerializer, EquipmentSerializer, RecipeIngredientSerializer, RecipeEquipmentSerializer, CuisineSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class RecipeEquipmentViewSet(viewsets.ModelViewSet):
    queryset = RecipeEquipment.objects.all()
    serializer_class = RecipeEquipmentSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
