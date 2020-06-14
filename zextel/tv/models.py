from django.db import models

# Create your models here.
class sm_channel(models.Model):
    sd = 'SD'
    hd = 'HD'
    k4 = '4K'
    format_choices = ((sd, 'SD'), (hd, 'HD'), (k4, '4K'))
    sub_4k = '4K'
    sub_kids = 'Детские'
    sub_film = 'Кино'
    sub_mus = 'Музыкальные'
    sub_news = 'Новостные'
    sub_smail = 'Развлекательные'
    sub_dick = 'Позновательные'
    sub_reg = 'Региональные'
    sub_sport = 'Спортивные'
    sub_efir = 'Эфирные'
    sub_choices = ((sub_4k, '4K'), (sub_kids, 'Детские'), (sub_film, 'Кино'), (sub_mus, 'Музыкальные'),
    (sub_news, 'Новостные'), (sub_smail, 'Развлекательные'), (sub_dick, 'Позновательные'),
    (sub_reg, 'Региональные'), (sub_sport,'Спортивные'), (sub_efir, 'Эфирные'))
    sm_title = models.CharField("Название канала", max_length=100)
    sm_sub = models.CharField("Тематика", choices=sub_choices, max_length=15)
    sm_format = models.CharField("Формат", choices=format_choices, max_length=3)

    class Meta:
        verbose_name = "Смотрешка канал"
        verbose_name_plural = "Смотрешка каналы"

    def __str__(self):
        return self.sm_title

class sm_spisok_ch(models.Model):
    sm_spisok_title = models.CharField("Наименование списка", max_length=100)
    sm_channel = models.ForeignKey(sm_channel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Список каналов"
        verbose_name_plural = "Списки каналов"

    def __str__(self):
        return self.sm_spisok_title

class sm_tarif(models.Model):
    sm_tarif_title = models.CharField("Наименование тарифа", max_length=100)
    sm_tarif_count = models.IntegerField("Количество каналов")
    sm_tarif_view = models.IntegerField("Количество устройств")
    sm_tarif_summ = models.IntegerField("Абонентская плата")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return self.sm_tarif_title
