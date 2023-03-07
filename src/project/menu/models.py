from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """
    The root for items
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "menu"


class Item(models.Model):
    """
    Any element in menu
    """

    name = models.CharField(max_length=100)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="items",
        null=False,
        blank=True,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    level = models.PositiveSmallIntegerField()

    # def get_absolute_url(self):
    #     return reverse('menu', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not hasattr(self, "menu"):
            self.menu = self.parent.menu

        if not self.parent:
            self.level = 0
        else:
            self.level = self.parent.level + 1

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent is not None:
            return f"{self.parent.name}->{self.name}"
        return self.name

    class Meta:
        verbose_name_plural = "items"
