from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
