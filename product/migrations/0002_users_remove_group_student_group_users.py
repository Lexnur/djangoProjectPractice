# Generated by Django 5.0.2 on 2024-02-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to='product.users', verbose_name='Студент'),
        ),
    ]
