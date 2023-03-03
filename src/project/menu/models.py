from django.db import models


class Menu(models.Model):
    """
    A root for items
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "menus"


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
    # need to add a validator for the root: the root can't have a parent.

    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if not hasattr(self, "menu"):
            self.menu = self.parent.menu
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent is not None:
            return f"{self.parent.name}->{self.name}"
        return self.name

    class Meta:
        verbose_name_plural = "items"
