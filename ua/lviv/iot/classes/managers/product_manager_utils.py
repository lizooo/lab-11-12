from ua.lviv.iot.classes.models.agegroup import AgeGroup
from ua.lviv.iot.classes.models.oil import Oil
from ua.lviv.iot.classes.models.shampoo import Shampoo
from ua.lviv.iot.classes.models.powder import Powder
from ua.lviv.iot.classes.models.sorttype import SortType
import doctest


class ProductManagerUtils:

    def __init__(self, list_of_all_products):
        self.list_of_all_products = list_of_all_products

    def sort_by_price_in_uah(self, sort_type):
        """
        Sorts List of Products in given order, returns List of Products
        >>> green_shampoo = Shampoo(AgeGroup.THREE_FOUR_YEARS, 210.0, "Johnson Baby", 300, 250.0, True)
        >>> baby_powder = Powder(AgeGroup.TEN_TWELVE_MONTH, 350.0, "Kids&Co", 120, 100.0, False)
        >>> lavander_oil = Oil(AgeGroup.THREE_SIX_MONTH, 100.5, "P&G", 360, 15.0, True)
        >>> product_list = [green_shampoo, baby_powder, lavander_oil]
        >>> prod_manager_utils = ProductManagerUtils(product_list)
        >>> list_of_products_sorted_by_price = prod_manager_utils.sort_by_price_in_uah(SortType.ASC)
        >>> [product.price_in_uah for product in list_of_products_sorted_by_price]
        [100.5, 210.0, 350.0]
        >>> list_of_products_sorted_by_price = prod_manager_utils.sort_by_price_in_uah(SortType.DSC)
        >>> [product.price_in_uah for product in list_of_products_sorted_by_price]
        [350.0, 210.0, 100.5]
        """
        if sort_type == SortType.ASC:
            list_of_products_sorted_by_price = sorted(self.list_of_all_products, key = lambda product: product.price_in_uah, reverse= False)
        if sort_type == SortType.DSC:
            list_of_products_sorted_by_price = sorted(self.list_of_all_products, key = lambda product: product.price_in_uah, reverse= True)
        return list_of_products_sorted_by_price

    def sort_by_producer(self, sort_type):
        """
        Sorts List of Products in given order, returns List of Products
        >>> green_shampoo = Shampoo(AgeGroup.THREE_FOUR_YEARS, 210.0, "Johnson Baby", 300, 250.0, True)
        >>> baby_powder = Powder(AgeGroup.TEN_TWELVE_MONTH, 350.0, "Kids&Co", 120, 100.0, False)
        >>> lavander_oil = Oil(AgeGroup.THREE_SIX_MONTH, 100.5, "P&G", 360, 15.0, True)
        >>> product_list = [green_shampoo, baby_powder, lavander_oil]
        >>> prod_manager_utils = ProductManagerUtils(product_list)
        >>> list_of_products_sorted_by_producer = prod_manager_utils.sort_by_producer(SortType.ASC)
        >>> [product.producer for product in list_of_products_sorted_by_producer]
        ['Johnson Baby', 'Kids&Co', 'P&G']
        >>> list_of_products_sorted_by_producer = prod_manager_utils.sort_by_producer(SortType.DSC)
        >>> [product.producer for product in list_of_products_sorted_by_producer]
        ['P&G', 'Kids&Co', 'Johnson Baby']
        """
        if sort_type == SortType.ASC:
            list_of_products_sorted_by_producer = sorted(self.list_of_all_products, key = lambda product: product.producer, reverse= False)
        if sort_type == SortType.DSC:
            list_of_products_sorted_by_producer = sorted(self.list_of_all_products, key = lambda product: product.producer, reverse= True)
        return list_of_products_sorted_by_producer


if __name__ == '__main__':
    doctest.testmod(verbose=True)

