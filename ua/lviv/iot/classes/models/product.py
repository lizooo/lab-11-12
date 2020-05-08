import datetime
from ua.lviv.iot.classes.models.agegroup import AgeGroup


class Product:
    def __init__(self, age_group=AgeGroup.ONE_TWO_MONTH, price_in_uah = 0.0, producer ="not specified", shelf_life_in_days = 0):
        self.age_group = age_group
        self.price_in_uah = price_in_uah
        self.producer = producer
        self.shelf_life_in_days = shelf_life_in_days

    def __str__(self):
        return ',\n'.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])+'\n'








