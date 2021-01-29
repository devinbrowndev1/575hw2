from DialogAct import DialogAct
from DialogActTypes import DialogActTypes

class NLGDefault:

    def __init__(self):
        # add whatever fields you want here
        self.Name = "NLGDefault"

    def generate(self, dialogAct):
        if (dialogAct.DialogActType == DialogActTypes.HELLO):
            return "Hello, how's it going?"
        elif (dialogAct.DialogActType == DialogActTypes.REQUEST):
            if dialogAct.info_type == "pizza_type":
                return "What type of pizza would you like?"
            elif dialogAct.info_type == "pizza_size":
                return "What size for this pizza?"
            elif dialogAct.info_type == "pizza_crust":
                return "What crust would you like?"
            elif dialogAct.info_type == "order_name":
                return "Can I get a name for this order?"
            elif dialogAct.info_type == "order_phone":
                return "What's a good phone number to reach you at?"
            elif dialogAct.info_type == "order_address":
                return "Where should we deliver the pizza to?"
            elif dialogAct.info_type == "order_delivery":
                return "Would you like pickup or delivery?"
            elif dialogAct.info_type == "confirmed":
                info = dialogAct.content.slots
                return "I have a {} {} pizza with {} crust. Does that look right?".format(info["pizza_size"],info["pizza_type"],info["pizza_crust"])
        elif (dialogAct.DialogActType == DialogActTypes.GOODBYE):
            return "Thanks for your order! Have a nice day."
