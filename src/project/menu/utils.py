def transform(data: tuple[dict]) -> list[dict]:
    """
    Из отсортированной (по полю level) последовательности словарей строит
    вложенную структуру в зависимости от предков
    """

    temp = {}
    result = []

    # id элементов меню, которые повторяются при выборке из бд из-за FULL JOIN.
    # TODO: возможно не нужно хранить в каждом item список id детей
    ids_of_temps = set()

    for raw_item in data:
        if temp.get(raw_item["id"]):
            ids_of_temps.add(raw_item["id"])
            continue

        item = {
            **raw_item,
            "expand": False,
            "childrens": {"ids": [], "items": []},
        }

        temp[item["id"]] = item
        if not item["parent"]:
            result.append(item)
        else:
            temp[item["parent"]]["childrens"]["ids"].append(item["id"])

            for children_id in ids_of_temps:
                if children_id == item["id"]:
                    ids_of_temps.remove(children_id)
                    temp[item["parent"]]["childrens"]["ids"].append(
                        children_id
                    )
            temp[item["parent"]]["childrens"]["items"].append(item)

    return result
