from django.contrib import admin

from .models import Author, Genre, Language, BookInstance, Book

# Register your models here.

# admin.site.register(BookInstance)
# admin.site.register(Author)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass