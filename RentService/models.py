import django.contrib.auth.backends
from django_jsonform.models.fields import ArrayField
from django.db import models
import datetime
from smart_selects.db_fields import ChainedForeignKey

types = [
    ('SP', 'Сап'),
    ('KK', 'Каяк'),
    ('KM', 'Катамаран'),
    ]


class Lake(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)

    class Meta:
        verbose_name = 'Озеро'
        verbose_name_plural = 'Озера'

    def __str__(self):
        return f'{self.name}'


class Beach(models.Model):
    lake = models.ForeignKey(Lake,verbose_name='Озеро',on_delete=models.CASCADE,null=True)
    name = models.CharField('Название', max_length=256, unique=True)
    features = ArrayField(models.CharField(blank=True), blank=True)

    class Meta:
        verbose_name = 'Пляж'
        verbose_name_plural = 'Пляжи'

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name='Название', max_length=256, unique=True)
    photo = models.ImageField('Фото', upload_to='Static/img/equipment/', default='Static/img/lake2.jpg')
    description = models.TextField('Описание', blank=True, null=True)
    is_active = models.BooleanField('Доступен?', default=True)
    classification = models.CharField('Вид инвентаря', choices=types, default='SP')
    cost_for_half_hour = models.IntegerField('30 минут', blank=True, default=0)
    cost_for_hour = models.IntegerField('1 час', blank=True, default=0)
    cost_for_3_hours = models.IntegerField('3 часа', blank=True, default=0)
    cost_for_day = models.IntegerField('Сутки', blank=True, default=0)\

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Список инвентаря'

    def __str__(self):
        return f'Название: {self.name}'


class Customer(models.Model):
    name = models.CharField('Имя', max_length=256, unique=True)
    phone = models.CharField('Номер', max_length=12, unique=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Имя: {self.name}'


class Schedule(models.Model):
    beaches = models.ManyToManyField(Beach)
    date = models.DateField('Дата', unique=True)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self):
        return f'{self.date}'


class Order(models.Model):
    lake = models.ForeignKey(Lake,on_delete=models.CASCADE,null=True)
    buyer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    equipment_id = ChainedForeignKey(Equipment,
                                     chained_field='beach',
                                     chained_model_field='beach',
                                     show_all=False,
                                     auto_choose=False,null=True)
    beach = ChainedForeignKey(Beach,
                              chained_field='lake',
                              chained_model_field='lake',
                              show_all=False,
                              auto_choose=False)
    start_time = models.DateTimeField('Время начала аренды')
    rent_time = models.FloatField('Время арнеды')
    cost = models.IntegerField('Стоимость заказа')
    comment = models.CharField('Комментарий', max_length=256, blank=True)
    rent_day = ChainedForeignKey(Schedule,
                                 chained_field='beach',
                                 chained_model_field='beaches',
                                 show_all=False,
                                 auto_choose=False,null=True)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.id}'