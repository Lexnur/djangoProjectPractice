from django.contrib import admin

from product.models import Product, Lesson, Group, Users


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'quantity_min', 'quantity_max')
    search_fields = ('name', 'author')
    list_filter = ('name', 'author', 'quantity_min', 'quantity_max')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    search_fields = ('name', 'product')
    list_filter = ('name', 'product')


admin.site.register(Group)


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'pay')
    search_fields = ('name',)
    list_filter = ('name', 'pay')

