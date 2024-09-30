"""
URL configuration for fridge_recipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RecipeViewSet, IngredientViewSet, SeasonViewSet, EquipmentViewSet, RecipeIngredientViewSet, RecipeEquipmentViewSet, CuisineViewSet


router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'recipe-ingredients', RecipeIngredientViewSet)
router.register(r'recipe-equipment', RecipeEquipmentViewSet)
router.register(r'cuisines', CuisineViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]
