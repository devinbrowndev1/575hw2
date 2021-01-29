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
        #self.prev_Dialog_Act = {} # Act_type, slot
        #self.reorder = False
        #self.check_info = {}
