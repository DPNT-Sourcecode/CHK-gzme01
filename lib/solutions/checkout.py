

PRODUCT_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

# I feel like I should have written a parser for the format I was given right at the beginning.
# Maybe if I'd have implemented the previous two challenges like this. I would have had the time to finish.

# noinspection PyUnusedLocal
# skus = unicode string


# As expected we need to move to a better model of managing the stores products
# and of implementing their offers.

# This is a list of products that do have discount offers
# The attached list is a representation of the offer
# The list is ordered so the offers can be applied in order.
# Larger discounts first.
DISCOUNT_MULTIBUY = {
    "A": [
        {
            "n": 5,
            "value": 50
        },
        {
            "n": 3,
            "value": 20
        }
    ],
    "B": [
        {
            "n": 2,
            "value": 15
        }
    ],
    "H": [
        {
            "n": 10,
            "value": 20
        },
        {
            "n": 5,
            "value": 5
        }
    ],
    "K": [
        {
            "n": 2,
            "value": 10
        }
    ],
    "P": [
        {
            "n": 5,
            "value": 50
        }
    ],
    "V": [
        {
            "n": 3,
            "value": 20
        },
        {
            "n": 2,
            "value": 10
        }
    ]
}

# It's going to take a while to write in all the correct products here.
# Going to make the free products model work first.

FREE_ITEM_MULTIBUY = {
    "E": [
        {
            "n": 2,
            "free_count": 1,
            "free_product": "B"
        }
    ],
    "F": [
        {
            "n": 3,
            "free_count": 1,
            "free_product": "F"
        }
    ],
    "N": [
        {
            "n": 3,
            "free_count": 1,
            "free_product": "M"
        }
    ],
    "R": [
        {
            "n": 3,
            "free_count": 1,
            "free_product": "Q"
        }
    ],
    "U": [
        {
            "n": 3,
            "free_count": 1,
            "free_product": "U"
        }
    ]
}


# This function figures out if any products have been made free through the pricing system
# It then removes them from the product count dictionary.
def remove_free_products(product_count):
    for product in FREE_ITEM_MULTIBUY.keys():
        for multibuy in FREE_ITEM_MULTIBUY[product]:
            number_made_free = min(product_count[product] / multibuy["n"], product_count[multibuy["free_product"]])
            product_count[multibuy["free_product"]] -= number_made_free
    return product_count


# Here we calculate the discount due to multibuys
def calculate_multibuy_discounts(product_count):
    total_discounts = 0

    for product in DISCOUNT_MULTIBUY.keys():
        for discount in DISCOUNT_MULTIBUY[product]:
            number_of_discounts = (product_count[product] / discount["n"])
            total_discounts += number_of_discounts * discount["value"]
            if product_count[product] >= discount["n"]:
                product_count[product] = product_count[product] - number_of_discounts * discount["n"]

    return total_discounts


# We could obviously have a different implementation if we needed
# to generate a receipt for the customer. But that isn't the aim of
# this function.
def checkout(skus):
    product_count = {key: 0 for (key, value) in PRODUCT_PRICES.items()}
    for product in skus:
        if product not in PRODUCT_PRICES.keys():
            return -1
        product_count[product] += 1

    product_count = remove_free_products(product_count)

    total_price = 0
    for product_sku, count in product_count.items():
        total_price += count * PRODUCT_PRICES[product_sku]

    discounts = calculate_multibuy_discounts(product_count)

    return total_price - discounts
