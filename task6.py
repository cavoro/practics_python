def merge_orders(web_orders: list, app_orders: list) -> list:
    result = []

    i = 0
    j = 0

    while i < len(web_orders) and j < len(app_orders):

        if web_orders[i] <= app_orders[j]:
            result.append(web_orders[i])
            i += 1
        else:
            result.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        result.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        result.append(app_orders[j])
        j += 1

    return result


web_orders = [1, 3, 5, 7]
app_orders = [2, 4, 6, 8]

print(merge_orders(web_orders, app_orders))
