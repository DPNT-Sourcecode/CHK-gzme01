

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
    number_discounts = product_count["E"] / 2
    return number_discounts * product_count["B"] * PRODUCT_PRICES["B"]


def price_for_product(sku, count):
    if (sku == "A"):
        # leftovers plus multibuys
        # Here we see how we could generalise the multibuy concept
        # We could go in stages. remainder = mod 5
        # then move on again.
        # This model doesn't extend to other offer types.
        # and does not accomodate further multibuys.
        price = 0
        remainder = count % 5
        price += ((count / 5) * 200)
        price += ((remainder / 3) * 130)
        price += ((remainder % 3) * PRODUCT_PRICES[sku])
        return price
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
        total_price += price_for_product(product_sku, count)

    discounts = calculate_discounts(product_count)

    return total_price - discounts


# Now we find out if the SKUs arrive as a simple string.
