from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Картинка', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='Владелец')

    def __str__(self):
        return f'{self.product_name} {self.description}'


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Наименование категории', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.category_name} {self.description}'


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='запись')
    picture = models.ImageField(upload_to="media/photos/%Y/%m/%d/", verbose_name='Картинка', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save()

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:blog_item', kwargs={'the_slug': self.slug})


class Version(models.Model):
    product_name = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='version',
                                     verbose_name='Наименование продукта')
    version_number = models.IntegerField(verbose_name='Номер версии', blank=True)
    version_name = models.CharField(max_length=255, verbose_name='Наименование версии')
    version_attribute = models.BooleanField(default=True, verbose_name='Статус версии')

    def __str__(self):
        return f"{self.version_name}"
