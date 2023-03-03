def transform(data):
    """
    transform values_list of Items into a dict with children field
    for each item
    """

    temp = {}
    result = []
    for raw_item in data:
        item = {
            "name": raw_item["name"],
            "parent__name": raw_item["parent__name"],
            "children": [],
        }

        temp[item["name"]] = item

        if not item["parent__name"]:
            result.append(item)
        else:
            temp[item["parent__name"]]["children"].append(item)

    return result


# def buildsubtrees(rows):
#     trees = {}

#     for row in rows:
#         trees.setdefault(
#             row["parent__id"], {}
#             )[row["name"]] = trees.setdefault(row["id"], {})


#     return trees