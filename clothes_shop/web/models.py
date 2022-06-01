from django.db import models

class Categories(models.Model):
    id = models.AutoField('id', primary_key=True )
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name
    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории!'

class Brands(models.Model):
    id = models.AutoField('id', primary_key=True )
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Type(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('name', max_length=55)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Size(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('name', max_length=55)
    type_product = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Products(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('title', max_length=200, default="")
    id_categories = models.ForeignKey('Categories', on_delete=models.SET_NULL, null=True)
    id_brand = models.ForeignKey('Brands', on_delete=models.SET_NULL, null=True)
    id_type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    img = models.ImageField(default="")
    price = models.IntegerField('price')
    size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    is_best_seller = models.BooleanField(default=False)
    is_new_arrivals = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.price
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'




