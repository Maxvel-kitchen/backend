# Generated by Django 4.1.4 on 2023-02-28 16:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
                ('order', models.IntegerField(default=0, help_text='По возрастанию', verbose_name='Очередность отображения')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('-order',),
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Цена')),
                ('new', models.BooleanField(default=False, verbose_name='Новинка!')),
                ('text', models.TextField(verbose_name='Описание')),
                ('ingredients', models.CharField(max_length=1024, verbose_name='Ингредиенты')),
                ('image', models.ImageField(blank=True, null=True, upload_to='position', verbose_name='Фото')),
                ('category', models.ManyToManyField(related_name='positions', to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='PositionForShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position', verbose_name='Позиция')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
                ('order', models.IntegerField(default=0, help_text='По возрастанию', verbose_name='Очередность отображения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ('-order',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_amount', models.IntegerField(verbose_name='Цена в итоге')),
                ('name_user', models.CharField(max_length=100, verbose_name='Клиент')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, verbose_name='Почта')),
                ('address', models.CharField(max_length=1024, verbose_name='Место мероприятия')),
                ('date_start', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('comment', models.CharField(max_length=1024, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания заявки')),
                ('positions_in_cart', models.ManyToManyField(to='api.positionforshoppingcart', verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AddField(
            model_name='position',
            name='sub_category',
            field=models.ManyToManyField(related_name='positions', to='api.subcategory', verbose_name='Подкатегория'),
        ),
    ]