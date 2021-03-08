from django.db import models

category_choices = [("other", "Разное"), ("flowers ", "Цветы"), ("toys", "Игрушки"), ("dishes", "Посуда") ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    category = models.CharField(max_length=40, choices=category_choices, default='other', verbose_name='Категория')
    balance = models.PositiveIntegerField(default=1, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2)
