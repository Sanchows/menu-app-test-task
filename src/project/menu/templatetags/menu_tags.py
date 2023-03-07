from django import template

from menu import utils
from menu.models import Item

from pprint import pprint


register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(name: str):
    menu = (
        Item.objects.select_related("parent")
        .values(
            "id",
            "name",
            "parent",
            "parent__name",
            "level"
        )
        .filter(menu__name=name)
        .order_by("level")
    )

    menu = utils.transform(tuple(menu))

    return {"menu": menu}
