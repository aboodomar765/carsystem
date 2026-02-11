from django.contrib import admin
from .models import Car, Sale, MonthlyExpense


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('chassis_number', 'car_type', 'year', 'purchase_value', 'status', 'user')
    list_filter = ('status', 'car_type', 'purchase_date')
    search_fields = ('chassis_number', 'user__username')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'sale_date', 'sale_value', 'partial_profit')
    list_filter = ('sale_date',)
    search_fields = ('car__chassis_number',)


@admin.register(MonthlyExpense)
class MonthlyExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'user')
    list_filter = ('date', 'user')
    search_fields = ('description', 'user__username')
