def transform(data):
    """
    transform values_list of Items into a dict with children field
    for each item
    """

    temp = {}
    result = []

    for raw_item in data:
        if temp.get(raw_item['name']):
            continue
        item = {
            "name": raw_item["name"],
            "parent__name": raw_item["parent__name"],
            "parent__id": raw_item["parent__id"],
            "childrens__name": raw_item["childrens__name"],
            "childrens_count": raw_item["childrens_count"],
            "id": raw_item["id"],
            "children": [],
        }

        temp[item["name"]] = item

        if not item["parent__name"]:
            result.append(item)
        else:
            temp[item["parent__name"]]["children"].append(item)

    return result
