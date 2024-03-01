from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта')
    author = models.CharField(max_length=150, verbose_name='Автор')
    datetime = models.DateTimeField(verbose_name='Дата и время старта')
    quantity_min = models.IntegerField(verbose_name='Минимальное количество студентов')
    quantity_max = models.IntegerField(verbose_name='Максимальное количество студентов')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    pay = models.BooleanField(default=False, verbose_name='Оплачено')  # Для отслеживания оплаты и доступа к продукту

    # group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, verbose_name='Группа')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=150, verbose_name='Группа')
    users = models.ManyToManyField(Users, verbose_name='Студент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['id']

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока')
    link = models.URLField(null=True, blank=True,  verbose_name='Ссылка на видео')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name
