from django.db import models
from users.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=60, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Продукт: {self.title} | Категория: {self.category}'
    

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    
    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email}| Продукт {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    

