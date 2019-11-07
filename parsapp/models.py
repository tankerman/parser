from django.db import models

# Create your models here.

class Address(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    info = models.ForeignKey('Info', on_delete=models.CASCADE, blank=True, null=True)

class Info(models.Model):
#     info = models.CharField(max_length=1000)
    area = models.CharField(max_length=50, blank=True, null=True, verbose_name='Площадь дома')
    stages = models.IntegerField(blank=True, null=True, verbose_name='Кол-во этажей')
    year_exp = models.CharField(max_length=50, blank=True, null=True, verbose_name='Год ввода в эксплуатацию')
    last_changes = models.CharField(max_length=50, blank=True, null=True, verbose_name='Последние изменения анкеты')
    year_build = models.CharField(max_length=50, blank=True, null=True, verbose_name='Год постройки')
    year_exp1 = models.CharField(max_length=50, blank=True, null=True, verbose_name='Год ввода в экспулатацию')
    serial = models.CharField(max_length=50, blank=True, null=True, verbose_name='Серия')
    house_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип дома')
    fond = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фонд кап ремонта')
    danger = models.CharField(max_length=50, blank=True, null=True, verbose_name='Аварийный')
    wall_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип перекрытия')
    wall_mat = models.CharField(max_length=50, blank=True, null=True, verbose_name='Материал стен')