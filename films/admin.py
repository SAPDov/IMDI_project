from django.contrib import admin
from .models import Category, Country, Film, Director


# Register your models here.
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Film)
admin.site.register(Director)

