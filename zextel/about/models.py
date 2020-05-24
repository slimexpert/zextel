from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class new(models.Model):
	new_title = models.CharField('Заголовок новости', max_length=100)
	new_title_text = models.CharField('Карткий текст', max_length=100)
	new_text = RichTextField('Полный текст', default="Поный текст")
	pub_date = models.DateTimeField('Дата публикации новости')
	pub_main = models.BooleanField('Показывать на главной', default=1)
	new_like = models.IntegerField('Лайк', default=1)

	def __str__(self):
		return self.new_title
	## Руссификация админки
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

class job(models.Model):
	job_title = models.CharField('Наименование вакансии', max_length=100)
	job_text = RichTextField('Полный текст вакансии', default="Вакансия")
	job_date = models.DateTimeField('Дата публикации вакансии')
	job_show = models.BooleanField('Отображать вакансию на сайте', default=1)

	def __str__(self):
		return self.new_title
	## Руссификация админки
	class Meta:
		verbose_name = 'Вакансия'
		verbose_name_plural = 'Вакансии'

class document(models.Model):
	doc_title = models.CharField('Заголовок документа', max_length=200)
	doc_path = models.CharField('Полный путь до документа', default="https://slimexpert.github.io/zextel/pdf/", max_length=250)
	doc_pub = models.DateTimeField('Дата публикации документа')
	doc_show = models.BooleanField('Отображать документ на сайте', default=1)

	def __str__(self):
		return self.new_title
	## Руссификация админки
	class Meta:
		verbose_name = 'Документ'
		verbose_name_plural = 'Документы'
