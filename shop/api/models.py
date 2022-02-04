from django.db import models
from treebeard.mp_tree import MP_Node
from django.core.validators import MinValueValidator


class Category(MP_Node):
    name = models.CharField(max_length=250, unique=True,
                            verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    node_order_by = ('name',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    scope = models.TextField(verbose_name='Сфера применения')
    diameter = models.FloatField(validators=[MinValueValidator(0.1)],
                                 verbose_name='Диаметр, мм')
    length = models.IntegerField(validators=[MinValueValidator(1)],
                                 verbose_name='Длина, мм')
    color = models.CharField(max_length=250, verbose_name='Цвет')
    image = models.ImageField(upload_to='products/',
                              verbose_name='Фото товара')
    card = models.ForeignKey(Category, on_delete=models.CASCADE,
                             related_name='products',
                             verbose_name='Карточка товара')

    class Meta:
        ordering = ('name', 'id')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}, длина {self.length}мм, диаметр {self.diameter}мм'
