from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Картинка', blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория', blank=True)
    price = models.IntegerField(verbose_name='Цена', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.product_name} {self.description}'


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Наименование категории', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.category_name} {self.description}'
