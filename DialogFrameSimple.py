class DialogFrameSimple:

    def __init__(self):
        self.FrameName = "DialogFrameSimple"
        # add whatever fields you want here
        self.slots = {"pizza_type": "",
                      "pizza_size": "",
                      "pizza_crust": "",
                      "pizza_cost": 0,
                      "order_name": "",
                      "order_phone": "",
                      "order_address": "",
                      "order_delivery": "",
                      "order_wait": 20,
                      "confirmed": False}
        self.restart = False
        self.wrong_info = False
        self.give_up = False
        self.repeat = False
        self.time = False
        self.prev_Dialog_Act = None # Act_type, slot
        self.reorder = False
        #self.check_info = {}
        self.prices = {"type":{"hawaiian": 6, "vegan": 8, "meat lovers":12.5, "4 cheese":6, "pepperoni":4, "veggie supreme":9.5},
                       "size":{"small":{"thin":10, "regular":10, "deep-dish":12, "gluten-free":15},
                               "medium":{"thin":12, "regular":12, "deep-dish":14, "gluten-free":18},
                               "large":{"thin":14, "regular":14, "deep-dish":18, "gluten-free":21}}}

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.slots["pizza_type"],self.slots["pizza_size"],self.slots["pizza_crust"],self.slots["order_name"],self.slots["order_phone"],self.slots["order_address"],self.slots["order_delivery"],)

    def calc_pizza_cost(self):
        self.slots['pizza_cost'] += self.prices['type'][self.slots['pizza_type']]
        self.slots['pizza_cost'] += self.prices['size'][self.slots['pizza_size']][self.slots['pizza_crust']]


    def build_from_database(self, saved_info):
        for slot in saved_info:
            self.slots[slot] = saved_info[slot]