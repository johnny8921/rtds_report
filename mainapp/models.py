from django.db import models
from django.utils import timezone

TYPE_CHOICES = (
    ('Стрелка', 'Стрелка'),
    ('Замедлитель', 'Замедлитель'),
    ('Путевой ящик', 'Путевой ящик'),
    ('Измеритель скорости (РИС)', 'Измеритель скорости (РИС)'),
)

STATE_CHOICES = {
    ('Установлен','Установлен'),
    ('В запасе','В запасе'),
    ('Есть сбои','Есть сбои'),
}

STATION_CHOICES = {
    ('Четная','Четная'),
    ('Нечетная','Нечетная'),

}

class Device(models.Model):
    factory_number = models.DecimalField(blank=False, null=False,max_digits=10, decimal_places=0, verbose_name="Заводской номер")
    device_type = models.CharField(max_length=25, blank=False , choices=TYPE_CHOICES, verbose_name="Тип устройства")
    factory_date = models.DateField(blank=True, null=True, verbose_name="Дата производства")
    work_date = models.DateField(blank=True, null=True, verbose_name="Дата Установки")
    work_station = models.CharField(max_length=25, blank=False , default="Четная", choices=STATION_CHOICES, verbose_name="Станция установки")
    work_number = models.CharField(blank=True, max_length=25, default="", verbose_name="место установки") 
    state = models.CharField(max_length=25, blank=False, default="В запасе", choices=STATE_CHOICES, verbose_name="Состояние")

    def publish(self):
        self.save()

    def __str__(self):

        if self.state == "В запасе":
            self.work_number = ""
            return (self.device_type + " " + self.state.lower())
        return (self.device_type + " " + str(self.work_number))

class Work(models.Model):
    factory_number = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=0, verbose_name="Заводской номер")
    date = models.DateField(blank=True, null=True, default=timezone.now, verbose_name="Дата работы")
    work_body = models.TextField(max_length=255, blank=True, null=True, verbose_name="Описание работы")

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.pk )