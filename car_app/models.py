from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'سيارة سيدان'),
        ('suv', 'سيارة SUV'),
        ('truck', 'شاحنة'),
        ('van', 'فان'),
        ('coupe', 'كوبيه'),
        ('hatchback', 'هاتشباك'),
    ]
    
    CLEARANCE_CHOICES = [
        ('purchase', 'شراء'),
        ('auction', 'إعلان'),
    ]
    
    STATUS_CHOICES = [
        ('available', 'غير مباع'),
        ('sold', 'مباع'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=150, verbose_name='اسم السيارة', null=True, blank=True, default='')
    car_type = models.CharField(max_length=50, choices=CAR_TYPE_CHOICES)
    year = models.IntegerField()
    chassis_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    clearance_type = models.CharField(max_length=20, choices=CLEARANCE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.chassis_number}"


class Sale(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='sale')
    sale_date = models.DateField()
    sale_value = models.DecimalField(max_digits=12, decimal_places=2)
    partial_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-sale_date']
    
    def __str__(self):
        return f"بيع {self.car} - {self.sale_date}"
    
    def get_total_profit(self):
        return self.sale_value - self.car.purchase_value


class MonthlyExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.description} - {self.amount} - {self.date}"
