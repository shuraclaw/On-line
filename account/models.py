from django.db import models

from products.models import Image


class UserInfo(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    fullName = models.CharField(max_length=200, verbose_name='ФИО', null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name='Почта', null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон', null=True, blank=True)
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Аватар', null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'

    def __str__(self):
        return self.user.username
