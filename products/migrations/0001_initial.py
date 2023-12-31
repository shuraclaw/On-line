# Generated by Django 4.2.1 on 2023-05-29 10:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('minPrice', models.IntegerField(default=0, verbose_name='Минимальная цена')),
                ('maxPrice', models.IntegerField(default=0, verbose_name='Максимальная цена')),
                ('freeDelivery', models.BooleanField(default=False, verbose_name='Бесплатная доставка')),
                ('available', models.BooleanField(default=False, verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=200, verbose_name='Путь к изображению')),
                ('alt', models.CharField(max_length=200, verbose_name='Описание изображения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(default=0, verbose_name='Категория')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('fullDescription', models.TextField(verbose_name='Полное описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('freeDelivery', models.BooleanField(default=False, verbose_name='Бесплатная доставка')),
                ('limited', models.BooleanField(default=False, verbose_name='Ограниченный товар')),
                ('images', models.ManyToManyField(blank=True, to='products.image', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('salePrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой')),
                ('dateFrom', models.DateField(verbose_name='Дата начала скидки')),
                ('dateTo', models.DateField(verbose_name='Дата окончания скидки')),
                ('images', models.ManyToManyField(blank=True, to='products.image', verbose_name='Изображения товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар со скидкой',
                'verbose_name_plural': 'Товары со скидкой',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, default='', max_length=100, verbose_name='Почта')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='products.review', verbose_name='Отзывы'),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ManyToManyField(blank=True, to='products.specification', verbose_name='Характеристики'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='products.tag', verbose_name='Теги'),
        ),
        migrations.CreateModel(
            name='CatalogItemSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название подкатегории')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.image', verbose_name='Изображение подкатегории')),
            ],
            options={
                'verbose_name': 'Подкатегория товаров в каталоге',
                'verbose_name_plural': 'Подкатегории товаров в каталоге',
            },
        ),
        migrations.CreateModel(
            name='CatalogItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название категории')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.image', verbose_name='Изображение категории')),
                ('subcategories', models.ManyToManyField(blank=True, to='products.catalogitemsubcategory', verbose_name='Подкатегории категории')),
            ],
            options={
                'verbose_name': 'Категория товаров в каталоге',
                'verbose_name_plural': 'Категории товаров в каталоге',
            },
        ),
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.image', verbose_name='Изображение товара')),
                ('subcategories', models.ManyToManyField(blank=True, to='products.catalogitemsubcategory', verbose_name='Подкатегории товара')),
            ],
            options={
                'verbose_name': 'Товар в каталоге',
                'verbose_name_plural': 'Товары в каталоге',
            },
        ),
    ]
