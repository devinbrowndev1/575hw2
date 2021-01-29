from DialogAct import DialogAct
from DialogActTypes import DialogActTypes

class NLGDefault:

    def __init__(self):
        # add whatever fields you want here
        self.Name = "NLGDefault"

    def generate(self, dialogAct):
        if dialogAct == None:
            return "Welcome to the Pizza Place. What can I get you?"

        if (dialogAct.DialogActType == DialogActTypes.HELLO):
            return "Welcome to the Pizza Place. What can I get you?"
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
                return "I have a {} {} pizza with {} crust for {}. It'll be ${} .Does that look right?".format(info["pizza_size"],info["pizza_type"],info["pizza_crust"],info["order_name"],info["pizza_cost"])
            elif dialogAct.info_type == "correction":
                return "I'm sorry, tell me what you'd like instead."
        elif dialogAct.DialogActType == DialogActTypes.INFORM:
            if dialogAct.info_type == "wait_time":
                info = dialogAct.content.slots
                return "About {} minutes".format(info["order_wait"])
        elif (dialogAct.DialogActType == DialogActTypes.GOODBYE):
            if dialogAct.info_type == "successful":
                return "Thanks for your order! Have a nice day. (Type Quit to exit)"
            else:
                return "Alright, goodbye. (Type Quit to exit)"
