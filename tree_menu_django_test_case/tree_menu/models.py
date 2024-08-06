from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название меню')
    url = models.SlugField(verbose_name='Ссылка на меню', unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("tree_menu:menu", kwargs={"menu_url": self.url})


class MenuItem(models.Model):
    menu = models.ForeignKey(
        to='Menu', on_delete=models.PROTECT, blank=True, null=True
    )

    parent = models.ForeignKey(
        to='MenuItem', on_delete=models.PROTECT, blank=True, null=True
    )

    url = models.SlugField(verbose_name='Ссылка на меню', unique=True)

    name = models.CharField(max_length=50, verbose_name='Название меню')

    def get_absolute_url(self):
        return reverse_lazy("tree_menu:menu", kwargs={"menu_url": self.url})

    def __str__(self) -> str:
        return self.name
