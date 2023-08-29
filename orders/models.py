from django.db import models

from products.models import *


class BasketProduct(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.IntegerField(default=0, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return self.product.title + ' - ' + str(self.count) + ' - ' + self.user.username


class Basket(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(BasketProduct, blank=True, verbose_name='Товары')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    category = models.IntegerField(default=0, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название')
    images = models.ManyToManyField(Image, blank=True, verbose_name='Изображения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    count = models.IntegerField(default=0, verbose_name='Количество')
    description = models.CharField(max_length=255, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    freeDelivery = models.BooleanField(default=False, verbose_name='Бесплатная доставка')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    reviews = models.ManyToManyField(Review, blank=True, verbose_name='Отзывы')

    @property
    def rating(self):
        if self.reviews.count() == 0:
            return 0
        else:
            return sum([review.rate for review in self.reviews.all()]) / self.reviews.count()

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    fullName = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.CharField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    deliveryType = models.CharField(max_length=100, verbose_name='Тип доставки')
    paymentType = models.CharField(max_length=100, verbose_name='Тип оплаты')
    products = models.ManyToManyField(OrderProduct, blank=True, verbose_name='Товары')

    @property
    def totalCost(self):
        return sum([product.price for product in self.products.all()])

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер')
    name = models.CharField(max_length=100, verbose_name='Название')
    month = models.IntegerField(default=0, verbose_name='Месяц')
    year = models.IntegerField(default=0, verbose_name='Год')
    code = models.IntegerField(default=0, verbose_name='Код')

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

    def __str__(self):
        return self.name
