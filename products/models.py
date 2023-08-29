from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Image(models.Model):
    src = models.CharField(max_length=200, verbose_name='Путь к изображению')
    alt = models.CharField(max_length=200, verbose_name='Описание изображения')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.alt


class CatalogItemSubcategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название подкатегории')
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, verbose_name='Изображение подкатегории', blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Подкатегория товаров в каталоге'
        verbose_name_plural = 'Подкатегории товаров в каталоге'

    def __str__(self):
        return self.title


class CatalogItemCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, verbose_name='Изображение категории', blank=True,
                              null=True)
    subcategories = models.ManyToManyField(CatalogItemSubcategory, blank=True, verbose_name='Подкатегории категории')

    class Meta:
        verbose_name = 'Категория товаров в каталоге'
        verbose_name_plural = 'Категории товаров в каталоге'

    def __str__(self):
        return self.title


class CatalogItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название товара')
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, verbose_name='Изображение товара', blank=True,
                              null=True)
    subcategories = models.ManyToManyField(CatalogItemSubcategory, blank=True, verbose_name='Подкатегории товара')

    class Meta:
        verbose_name = 'Товар в каталоге'
        verbose_name_plural = 'Товары в каталоге'

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    email = models.CharField(max_length=100, default='', verbose_name='Почта', blank=True)
    text = models.CharField(max_length=255, verbose_name='Текст')
    rate = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)],
                               verbose_name='Оценка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:30] + '...' + ' - ' + str(self.rate) + ' stars'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Specification(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    value = models.CharField(max_length=100, verbose_name='Значение')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name + ' - ' + self.value


class Product(models.Model):
    category = models.IntegerField(default=0, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название')
    images = models.ManyToManyField(Image, blank=True, verbose_name='Изображения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    count = models.IntegerField(default=0, verbose_name='Количество')
    description = models.CharField(max_length=255, verbose_name='Описание')
    fullDescription = models.TextField(verbose_name='Полное описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    freeDelivery = models.BooleanField(default=False, verbose_name='Бесплатная доставка')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    reviews = models.ManyToManyField(Review, blank=True, verbose_name='Отзывы')
    specifications = models.ManyToManyField(Specification, blank=True, verbose_name='Характеристики')

    limited = models.BooleanField(default=False, verbose_name='Ограниченный товар')

    @property
    def rating(self):
        if self.reviews.count() == 0:
            return 0
        else:
            return sum([review.rate for review in self.reviews.all()]) / self.reviews.count()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title + ' - $' + str(self.price)


class SaleItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    images = models.ManyToManyField(Image, blank=True, verbose_name='Изображения товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    salePrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                    verbose_name='Цена со скидкой')
    dateFrom = models.DateField(verbose_name='Дата начала скидки')
    dateTo = models.DateField(verbose_name='Дата окончания скидки')

    class Meta:
        verbose_name = 'Товар со скидкой'
        verbose_name_plural = 'Товары со скидкой'

    def __str__(self):
        return self.product.title + ' - $' + str(self.salePrice)


class Filter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    minPrice = models.IntegerField(default=0, verbose_name='Минимальная цена')
    maxPrice = models.IntegerField(default=0, verbose_name='Максимальная цена')
    freeDelivery = models.BooleanField(default=False, verbose_name='Бесплатная доставка')
    available = models.BooleanField(default=False, verbose_name='В наличии')

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'

    def __str__(self):
        return self.name
