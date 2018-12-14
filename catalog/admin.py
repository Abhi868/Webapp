from django.contrib import admin

# Register your models here.
from catalog.models import Genre,Movies,CustomUser

admin.site.register(Movies)
admin.site.register(Genre)
admin.site.register(CustomUser)
