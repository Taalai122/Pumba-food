# Generated by Django 5.0.6 on 2024-07-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField(verbose_name='Наша история')),
                ('why_us', models.TextField(verbose_name='Почему мы')),
                ('image', models.ImageField(upload_to='about_us', verbose_name='Фото работников')),
                ('employees_name', models.CharField(max_length=255, verbose_name='Имя работника')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]