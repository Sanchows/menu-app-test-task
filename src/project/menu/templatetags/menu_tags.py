from django import template
from django.db.models import Count

from menu import utils
from menu.models import Item

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(name: str):
    menu = (
        Item.objects.select_related("parent", "childrens")
        .values(
            "id",
            "name",
            "parent__id",
            "parent__name",
            "childrens__name",
        )
        .annotate(childrens_count=Count("childrens"))
        .filter(menu__name=name)
    )

    menu = utils.transform(
        sorted(menu, key=lambda x: x["childrens_count"], reverse=True)
    )

    return {"menu": menu}
