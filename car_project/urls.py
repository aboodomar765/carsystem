from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from car_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='car_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Car URLs
    path('cars/', views.car_list, name='car_list'),
    path('cars/export/pdf/', views.export_cars_pdf, name='export_cars_pdf'),
    path('cars/add/', views.add_car, name='add_car'),
    path('cars/<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('cars/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('cars/<int:car_id>/add-sale/', views.add_sale, name='add_sale'),
    
    # Sales URLs
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/export/pdf/', views.export_sales_pdf, name='export_sales_pdf'),
    path('sales/export/excel/', views.export_sales_excel, name='export_sales_excel'),
    path('sales/<int:sale_id>/edit/', views.edit_sale, name='edit_sale'),
    
    # Expenses URLs
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    
    # API URLs
    path('api/cars/', views.api_car_list, name='api_car_list'),
    path('api/sales/', views.api_sales_list, name='api_sales_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
