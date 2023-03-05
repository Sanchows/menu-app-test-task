def transform(data):
    """
    transform values_list of Items into a dict with children field
    for each item
    """

    temp = {}
    result = []

    for raw_item in data:
        if temp.get(raw_item["name"]):
            continue

        item = {
            "name": raw_item["name"],
            "parent__name": raw_item["parent__name"],
            "parent": raw_item["parent"],
            "children__name": raw_item["children__name"],
            "children": raw_item["children"],
            "id": raw_item["id"],
            "childrens": [],
        }

        temp[item["name"]] = item

        if not item["parent__name"]:
            result.append(item)
        else:
            temp[item["parent__name"]]["childrens"].append(item)

    return result
