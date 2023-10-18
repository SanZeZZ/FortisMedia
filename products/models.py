from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.CharField('Почта', max_length=20)
    number = models.CharField('Номер', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'