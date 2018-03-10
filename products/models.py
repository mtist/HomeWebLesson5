from django.db import models


class Catalog(models.Model):
    title = models.CharField('Название каталога', max_length=100)
    slug = models.SlugField(max_length=100)


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    slug = models.SlugField(max_length=100)
    catalog = models.ForeignKey(Catalog, verbose_name='Каталога', on_delete=models.CASCADE)
    price = models.IntegerField('Цена продукта')
    mass = models.IntegerField('Вес продукта')
    picture = models.ImageField('Фото продукта')
    manufacturer = models.CharField('Производитель', max_length=100)
    # напишите другие поля: цена вес картинка и тп в зависимости от продукции. Минимум 4 поля
    # какие бывают типы полей можете почитать тут: https://djbook.ru/rel1.9/ref/models/fields.html

    def __str__(self):
        return self.title
