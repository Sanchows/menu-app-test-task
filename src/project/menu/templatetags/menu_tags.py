from django import template

from menu import utils
from menu.models import Item

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(name: str):
    menu = (
        Item.objects.select_related("parent", "children")
        .values(
            "id",
            "name",
            "parent",
            "parent__name",
            "children__name",
            "children",
            "level"
        )
        .filter(menu__name=name)
        .order_by("level")
    )

    menu = utils.transform(menu)

    return {"menu": menu}
