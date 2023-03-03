from django import template

from menu import utils
from menu.models import Item

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(name: str):
    menu = (
        Item.objects.select_related("parent", "menu__items")
        .values(
            "id",
            "name",
            "parent__id",
            "parent__name",
        )
        .filter(menu__name=name)
    )
    res = utils.transform(menu)

    return {"menu": res}
