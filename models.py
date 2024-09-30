from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100, choices=[('Africa', 'Africa'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('South America', 'South America'), ('Australia', 'Australia'), ('Antarctica', 'Antarctica')])

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=50)
    start_month = models.IntegerField()
    end_month = models.IntegerField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    seasonal = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return f"{self.amount} of {self.ingredient.name} for {self.recipe.title}"

class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeEquipment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_equipment', on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipment.name} for {self.recipe.title}"
