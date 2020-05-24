from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

# Модель для слайдера
class slider(models.Model):
	sl_title = models.CharField("Название слайдера", max_length=100)
	sl_number = models.IntegerField("Очередность вывода слайдера")
	sl_text = RichTextField('HTML сладера', default="<div></div>")
	sl_show = models.BooleanField('Показывать слайдер', default=1)

	class Meta:
		verbose_name = "Слайдер"
		verbose_name_plural = "Слайдеры"

	def __str__(self):
		return self.sl_title

# Модель для обращений
class contact_support(models.Model):
	supp_name = models.CharField("Имя отправителя", max_length=50)
	supp_email = models.EmailField("E-mail отправителя", max_length=100)
	supp_tel = models.CharField("Телефон отправителя", max_length=14)
	supp_cat = models.CharField("Категория обращения", max_length=50)
	supp_text = models.TextField('Текст обращения')
	supp_otvet  = models.CharField('Ответ на обращение', max_length=50)
	supp_date = models.DateTimeField('Дата обращения', auto_now_add=True)

	def get_absolute_url(self):
		return reverse('main:support_url', kwargs={'supp_name':self.supp_name})

	class Meta:
		verbose_name = "Обращение"
		verbose_name_plural = "Обращения"

	def __str__(self):
		return '{}'.format(self.supp_name)

# Модель для зон охвата сети
class zone(models.Model):
	zone_title = models.CharField("Наименование зоны", max_length=100)
	zone_text = models.CharField("Описание", max_length=200)
	zone_summ = models.IntegerField("Стоимость", blank=True, default="6000")
	zone_show = models.BooleanField('Учитывать', default=1)
	zone_number = models.IntegerField("Порядок вывода", blank=True, default="1")

	class Meta:
		verbose_name = "Зона охвата"
		verbose_name_plural = "Зоны охвата"

	def __str__(self):
		return self.zone_title

# Модель для Индексов
class postal(models.Model):
	postal_code = models.CharField("Индекс", max_length=6, blank=True)
	postal_title = models.CharField("Наименование", max_length=150)
	postal_show = models.BooleanField('Учитывать', default=1)
	postal_zone = models.ForeignKey(zone, on_delete=models.PROTECT)

	class Meta:
		verbose_name = "Населенный пункт"
		verbose_name_plural = "Населенные пункты"

	def __str__(self):
		return self.postal_title

# Модель для Тарифов
class Rate(models.Model):
	mkd = 'МКД'
	dom = 'ЧД'
	type_rate_choices = ((mkd, 'Многоквартирный дом'), (dom, 'Частный дом'))

	rate_title = models.CharField("Название тарифа", max_length=100)
	rate_title_text = models.CharField("Описание тарифа", max_length=100)
	rate_zone = models.ForeignKey(zone, on_delete=models.PROTECT)
	rate_group = models.IntegerField("Группа тарифов")
	rate_number = models.IntegerField("Номер тарифа в группе")
	rate_type = models.CharField('Тип тарифа', choices=type_rate_choices, max_length=50)
	rate_popular = models.BooleanField('Выделения популяр. тарифа', default=0)
	rate_speed = models.IntegerField("Скорость доступа")
	rate_summ = models.FloatField("Стоимость")
	rate_rate = models.FloatField("Рейтинг тарифа от 0 до 5")
	rate_tv_show = models.BooleanField('Показывать ТВ каналы', default=0)
	rate_tv_count = models.IntegerField("Количество каналов")

	class Meta:
		verbose_name = "Тарифный план"
		verbose_name_plural = "Тарифные планы"

	def __str__(self):
		return self.rate_title
