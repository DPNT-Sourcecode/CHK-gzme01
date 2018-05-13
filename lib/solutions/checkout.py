

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


def calculate_discounts(product_count):

    total_discounts = 0
    number_E_B_discounts = product_count["E"] / 2
    total_discounts += min(number_E_B_discounts, product_count["B"]) * PRODUCT_PRICES["B"]

    remainder_A = product_count["A"] % 5
    total_discounts += ((product_count["A"] / 5) * 50)
    total_discounts += ((remainder_A / 3) * 20)

    total_discounts += (product_count["B"] * 15)

    return total_discounts


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
        total_price += count * PRODUCT_PRICES[product_sku]

    discounts = calculate_discounts(product_count)

    return total_price - discounts


# Now we find out if the SKUs arrive as a simple string.
