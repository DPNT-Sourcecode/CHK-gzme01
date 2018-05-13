

PRODUCT_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

# noinspection PyUnusedLocal
# skus = unicode string

# Not necessarily the best way of doing this


def calculate_price(sku, count):
    if (sku == "A"):
        # leftovers plus multibuys
        # Here we see how we could generalise the multibuy concept
        # We could go in stages. remainder = mod 5
        # then move on again.
        p
        remainder = count % 5
        return ((count % 3) * PRODUCT_PRICES[sku]) + ((count / 3) * 130)
    elif (sku == "B"):
        return ((count % 2) * PRODUCT_PRICES[sku]) + ((count / 2) * 45)
    else:
        return count * PRODUCT_PRICES[sku]


def checkout(skus):
    product_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0
    }
    for product in skus:
        if product not in PRODUCT_PRICES.keys():
            return -1
        product_count[product] += 1

    total_price = 0
    for product_sku, count in product_count.items():
        total_price += calculate_price(product_sku, count)

    return total_price


# Now we find out if the SKUs arrive as a simple string.
