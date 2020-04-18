from django.db import models
from ckeditor.fields import RichTextField

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
	supp_email = models.EmailField("E-mail", max_length=100)
	

	class Meta:
		verbose_name = "Обращение"
		verbose_name_plural = "Обращения"

	def __str__(self):
		return self.sl_title
    
