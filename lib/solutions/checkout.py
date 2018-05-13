

PRODUCT_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10
}

# noinspection PyUnusedLocal
# skus = unicode string


# As expected we need to move to a better model of managing the stores products
# and of implementing their offers.

# This is a list of products that do have discount offers
# The attached list is a representation of the offer
# The list is ordered so the offers can be applied in order.
# Larger discounts first.
DISCOUNT_MULTIBUY = {
    # "A": [
    #     {
    #         "n": 5,
    #         "discount": 50
    #     },
    #     {
    #         "n": 3,
    #         "discount": 20
    #     }
    # ],
    "B": [
        {
            "n": 2,
            "discount": 15
        }
    ]
}


# This function figures out if any products have been made free through the pricing system
# It then removes them from the product count dictionary.
def remove_free_products(product_count):
    number_E_B_discounts = product_count["E"] / 2
    product_count["B"] = product_count["B"] - min(number_E_B_discounts, product_count["B"])
    number_F_made_free = product_count["F"] / 3
    product_count["F"] = product_count["F"] - number_F_made_free
    return product_count


def calculate_discounts(product_count):
    total_discounts = 0
    # Here we calculate the discount due to multibuys
    remainder_A = product_count["A"] % 5
    total_discounts += ((product_count["A"] / 5) * 50)
    total_discounts += ((remainder_A / 3) * 20)

    for product in DISCOUNT_MULTIBUY.keys():
        print("--------------->>>>>>>>>>>>>---------------")
        print(product_count[product])
        print("---------------<<<<<<<<<<<<<---------------")

    return total_discounts


# We could obviously have a different implementation if we needed
# to generate a receipt for the customer. But that isn't the aim of
# this function.
def checkout(skus):
    product_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0
    }
    for product in skus:
        if product not in PRODUCT_PRICES.keys():
            return -1
        product_count[product] += 1

    product_count = remove_free_products(product_count)

    total_price = 0
    for product_sku, count in product_count.items():
        total_price += count * PRODUCT_PRICES[product_sku]

    discounts = calculate_discounts(product_count)

    return total_price - discounts
