from django.contrib import admin
from recipe.models import Category, Recipe, Ingredient

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)