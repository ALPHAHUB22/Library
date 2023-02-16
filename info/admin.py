from django.contrib import admin
from .models import Library
# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    list_display = ["book_id", "name", "price"]

admin.site.register(Library, LibraryAdmin)