from ua.lviv.iot.classes.models.product import Product
from ua.lviv.iot.classes.models.agegroup import AgeGroup


class Shampoo(Product):
    def __init__(self, price_in_uah = 0.0, producer = "not specified",
                 shelf_life_in_days = 0, value_in_ml = 0.0, is_for_sensitive_eyes = False):
        super().__init__( price_in_uah, producer, shelf_life_in_days)
        self.value_in_ml = value_in_ml
        self.is_for_sensitive_eyes = is_for_sensitive_eyes


