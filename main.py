from pizzaOrderFrame import pizzaOrderFrame
from pizzaFrame import pizzaFrame
from NLUDefaultFrame import NLU


"""state_building_list = [
["add_pizza","Welcome to the pizza ordering system.\nTo cancel at anytime type: cancel\nTo repeat order at anytime type: repeat\nTo start over at any time, type: start over\nWhat specialty pizza would you like?","hawaiian:change_size","vegan:change_size"]
,["change_size","What size? (small,medium,large)","large:change_crust","medium:change_crust","small:change_crust"]
,["change_crust","What type of crust? (thin,deepdish,gluten-free)","regular:delivery_type","thin:delivery_type","deepdish:delivery_type","gluten-free:delivery_type"]
,["delivery_type","Pick-up or delivery?","delivery:add_address","pickup:add_name"]
,["add_address","What is your address?","address:add_name"]
,["add_name","Can I get a name for the order?","name_val:add_phone"]
,["add_phone","Phone number?","phone_num:check_order"]
,["check_order","Got your order.","yes_regex:confirm_order","no_regex:misunderstood_pizza"]
,["misunderstood_pizza","I'm sorry, here's what you asked for ___. Should we restart this pizza?","yes_regex:add_pizza","no_regex:confirm_order"]
,["cancel", "We've cancelled your order, have a nice day"]]
"""

pizza_slot_request = ["What type of pizza do you want?",
                      "What size pizza would you like?",
                      "What crust do you want on your pizza?"]

order_slot_request = ["What kind of pizza do you want?",
                      "What is your name?",
                      "Do you want pickup or delivery?",
                      "What is your address?",
                      "What is your phone number?"]


#initialize pizzaOrder and pizza
order_x = pizzaOrderFrame()
pizza_x = pizzaFrame()
parser = NLU()

orderIncomplete = True
pizza_values = ["add_pizza", "change_size", "change_crust"]
pizza_complete = [1,1,1]
order_complete = [1,1,1,1,1]

while orderIncomplete:
    if pizza_x.completed == pizza_complete:
        order_x.add_pizza(pizza_x)
        if order_x.completed == order_complete:
            orderIncomplete = False
            break

    asked_for_info = False

    for i, x in enumerate(pizza_x.completed):
        if x == 0 and not asked_for_info:
            print(pizza_slot_request[i])
            asked_for_info = True

    for i,x in enumerate(order_x.completed):
        if x == 0 and not asked_for_info:
            print(order_slot_request[i])
            asked_for_info = True

    in_value = input().strip()

    slot_list = parser.parse(in_value)

    for slot in slot_list:
        value, info_type = slot

        if info_type in pizza_values:
            pizza_x.set_pizza_info(info_type, value)
        else:
            order_x.set_order_info(info_type, value)

    print(pizza_x)
    try:
        print(order_x)
    except:
        print("")


print("Thanks for your order!")
