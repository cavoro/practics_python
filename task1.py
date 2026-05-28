def find_product(products: list, target: str) -> int:
    for i in range(len(products)):
        if products[i] == target:
            return i + 1
    return -1


products = ["Ноутбук", "Мишка", "Клавіатура", "Монітор"]

result = find_product(products, "Клавіатура")

if result != -1:
    print(result)
else:
    print("Товар не знайдено")
