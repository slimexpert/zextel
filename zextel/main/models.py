from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class slider(models.Model):
	sl_title = models.CharField("Название слайдера", max_length=100)
	sl_number = models.IntegerField("Очередность вывода слайдера")
	sl_text = RichTextField('HTML сладера', default="<div></div>")
	sl_show = models.BooleanField('Показывать слайдер', default=1)

def __str__(self):
    return self.sl_title

## Руссификация админки
    class Meta:
    	verbose_name = 'Слайдер'
    	verbose_name_plural = 'Слайдеры'