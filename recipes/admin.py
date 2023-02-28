from django.contrib import admin
from recipes.models import Category
from recipes.models import Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    admin.site.register(Category)

class RecipeAdmin(admin.ModelAdmin):
    admin.site.register(Recipe)