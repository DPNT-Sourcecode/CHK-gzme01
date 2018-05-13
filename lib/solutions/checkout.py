

PRODUCTS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    product_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    for product in skus:
        product_count[product] += 1

    print(product_count)
    return 0
