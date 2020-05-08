from typing import List

from ua.lviv.iot.classes.models.agegroup import AgeGroup
from ua.lviv.iot.classes.models.oil import Oil
from ua.lviv.iot.classes.models.shampoo import Shampoo
from ua.lviv.iot.classes.models.powder import Powder
from ua.lviv.iot.classes.models.product import Product
import doctest


class ProductManager:
    def __init__(self):
        self.list_of_all_products = []

    def find_product_by_age_group(self, age_group_for_search):
        """
        looks for products with given age group returns list of found products
        >>> product_manager = ProductManager()
        >>> product_manager.list_of_all_products.append(Shampoo(AgeGroup.ONE_TWO_YEARS, 90.0, "p&g", 90, 30.0, True))
        >>> product_manager.list_of_all_products.append(Oil(AgeGroup.TEN_TWELVE_MONTH, 120.0, "P&G", 600, 350.0, False))
        >>> product_manager.list_of_all_products.append(Powder(AgeGroup.ONE_TWO_YEARS, 150.0, "Prostor", 450, 300.0, True))
        >>> list_of_found_products = product_manager.find_product_by_age_group(AgeGroup.ONE_TWO_YEARS)
        >>> len(list_of_found_products)
        2
        """
        list_of_found_products: List[Product] = []
        for product in self.list_of_all_products:
            if product.age_group == age_group_for_search:
                list_of_found_products.append(product)
        return list_of_found_products

    def find_product_with_price(self, price_for_search):
        """
        looks for products with given age group returns list of found products
        >>> product_manager = ProductManager()
        >>> product_manager.list_of_all_products.append(Shampoo(AgeGroup.ONE_TWO_YEARS, 90.0, "p&g", 90, 30.0, True))
        >>> product_manager.list_of_all_products.append(Oil(AgeGroup.TEN_TWELVE_MONTH, 120.0, "P&G", 600, 350.0, False))
        >>> product_manager.list_of_all_products.append(Powder(AgeGroup.ONE_TWO_YEARS, 150.0, "Prostor", 450, 300.0, True))
        >>> list_of_found_products = product_manager.find_product_with_price(120.0)
        >>> [product.price_in_uah for product in list_of_found_products]
        [120.0]
        """
        list_of_found_products = []
        for product in self.list_of_all_products:
            if product.price_in_uah == price_for_search:
                list_of_found_products.append(product)
        return list_of_found_products


if __name__ == '__main__':
    doctest.testmod(verbose=True)