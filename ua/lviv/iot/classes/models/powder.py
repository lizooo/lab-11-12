from ua.lviv.iot.classes.models.product import Product


class Powder(Product):
    def __init__(self, price_in_uah=0.0, producer="not specified",
                 shelf_life_in_days=0, value_in_grams =0.0, is_translucent = False):
        super().__init__(price_in_uah, producer, shelf_life_in_days)
        self.value_in_grams = value_in_grams
        self.is_translucent = is_translucent

