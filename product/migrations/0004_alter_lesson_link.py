# Generated by Django 5.0.2 on 2024-03-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_group_pay_users_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.URLField(null=True, verbose_name='Ссылка на видео'),
        ),
    ]
