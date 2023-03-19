from django.contrib import admin

# from .models import (Category, Ingredient, PositionForShoppingCart, Position,
#                      ShoppingCart)
from .models import (Category, Position, PositionForShoppingCart, ShoppingCart,
                     SubCategory)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


# class IngredientAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk',
#         'name',
#         'measurement_unit',
#         'amount',
#     )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'price',
        'text',
    )
    ordering = 'pk',


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        # 'positions',
        'all_amount',
        'name_user',
        'phone',
        'email',
        'address',
        'date_start',
        'comment',
        'pub_date',
    )


@admin.register(PositionForShoppingCart)
class PositionForShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'position',
        'amount',
    )


# admin.site.register(Ingredient, IngredientAdmin)
