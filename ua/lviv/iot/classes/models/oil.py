from ua.lviv.iot.classes.models.product import Product


class Oil(Product):
    def __init__(self, age_group, price_in_uah = 0.0, producer = "not specified",
                 shelf_life_in_days = 0, value_in_ml = 0.0, is_for_sensitive_skin = False):
        super().__init__(age_group, price_in_uah, producer, shelf_life_in_days)
        self.value_in_ml = value_in_ml
        self.is_for_sensitive_skin = is_for_sensitive_skin

