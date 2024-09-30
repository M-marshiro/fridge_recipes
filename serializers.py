from rest_framework import serializers
from .models import Recipe, Ingredient, Season, Equipment, RecipeIngredient, RecipeEquipment, Cuisine

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'continent']

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'name', 'start_month', 'end_month']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'amount', 'seasonal']

class RecipeEquipmentSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer()

    class Meta:
        model = RecipeEquipment
        fields = ['id', 'recipe', 'equipment']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    equipment = RecipeEquipmentSerializer(many=True, read_only=True)
    cuisine = serializers.StringRelatedField()  

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'cuisine', 'created_at', 'ingredients', 'equipment']

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name']
