from django.contrib import admin
from .models import Category, ToDoList
from . import models
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created_time", "due_time")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
# admin.site.register(ToDoList)
# admin.site.register(Category)
admin.site.register(models.ToDoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)