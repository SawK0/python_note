# ########## CLASS ########### #
import math


class Item:
    def calc_total_price(self, x, y):  # self - python passes the object itself as a first argument
        return x * y


item1 = Item()
item1.price = 100
item1.quantity = 5


# print(item1.calc_total_price(item1.price, item1.quantity))


# ################## OOP ################# #
# -------------- Magic Method --------------------- #

class MagicMethod:
    def __init__(self, name):  # init method initiate the class
        self.name = name


