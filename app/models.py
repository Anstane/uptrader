from django.db import models

class MenuItem(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    url = models.CharField(
        max_length=255,
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children' 
    )

    class Meta:
        verbose_name = 'Предмет - меню'
        verbose_name_plural = 'Предметы - меню'

    def __str__(self):
        return self.name
