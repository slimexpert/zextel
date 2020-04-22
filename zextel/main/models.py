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
