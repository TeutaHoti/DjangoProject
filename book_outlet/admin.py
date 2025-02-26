from django.contrib import admin
from .models import Book, Author, Address, Country



class BookAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",)}
    list_display = ('author','rating',)
    list_display = ('title',"author",)
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
# Register your models here.
