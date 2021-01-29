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

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.slots["pizza_type"],self.slots["pizza_size"],self.slots["pizza_crust"],self.slots["order_name"],self.slots["order_phone"],self.slots["order_address"],self.slots["order_delivery"],)

    def build_from_database(self, saved_info):
        for slot in saved_info:
            self.slots[slot] = saved_info[slot]