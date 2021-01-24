import sys
import re
import nltk
from state import state
from pizzaOrder import pizzaOrder
from pizza import pizza
from NLUDefault import NLU


state_building_list = [
["add_pizza","Welcome to the pizza ordering system.\nPizzaBot:To cancel at anytime type: cancel, To repeat order at anytime type: repeat\nPizzaBot:What specialty pizza would you like?","hawaiian:change_size","vegan:change_size"]
,["change_size","What size? (small,medium,large)","large:change_crust","medium:change_crust","small:change_crust"]
,["change_crust","What type of crust? (thin,deepdish,gluten-free)","regular:delivery_type","thin:delivery_type","deepdish:delivery_type","gluten-free:delivery_type"]
,["delivery_type","Pick-up or delivery?","delivery:get_address","pickup:add_name"]
,["get_address","What is your address?","address:add_name"]
,["add_name","Can I get a name for the order?","name_val:add_phone"]
,["add_phone","Phone number?","phone_num:check_order"]
,["check_order","Got your order.","yes_regex:confirm_order","no_regex:misunderstood_pizza"]
,["misunderstood_pizza","I'm sorry, here's what you asked for ___. Should we restart this pizza?","yes_regex:add_pizza","no_regex:confirm_order"]]



#list of built states
fsm = {}
for s in state_building_list:
    temp = state()
    temp.build_state(s)
    fsm[temp.state_name] = temp

#print(fsm["add_pizza"])


#initialize pizzaOrder and pizza
order_x = pizzaOrder()
pizza_x = pizza()
parser = NLU()

currState = "add_pizza"

while currState != 'confirm_order':

    # Prompt user for input
    print(fsm[currState].sys_out)

    if currState == 'check_order':
        print(order_x,'Is this okay? (Y/N)')

    # Get input from user
    in_value = input().lower().strip()

    user_info, next_state = parser.parse(fsm[currState], in_value)

    #start, what kind of pizza? vegan
    #add_pizza, what size? small
    #change_size, what crust? thin
    #change_crust, pickup or delivery? pickup
    #delivery_type, name? jessica
    #add_name, phone number? 123
    #add_phone, is this order okay? yes
    #confirm_order

    # Save their input in the order
    if currState == "add_pizza":
        pizza_x.set_pizza_info(currState, user_info)

    elif currState == "change_size":
        pizza_x.set_pizza_info(currState, user_info)

    elif currState == "change_crust":
        pizza_x.set_pizza_info(currState, user_info)
        order_x.add_pizza(pizza_x)
        order_x.set_cost_of_pizzas()

    elif currState == "delivery_type":
        order_x.set_order_info(currState, user_info)

    elif currState == "add_name":
        order_x.set_order_info(currState, user_info)

    elif currState == "add_phone":
        order_x.set_order_info(currState, user_info)

    # Change state
    currState = next_state

print("Order confirmed. Have a nice day!")



    #all of this goes into regex


    # if currState == 'add_phone':
    #     print('PizzaBot: Here is your order:')
    #     order_x.set_cost_of_pizzas()
    #     order_x.set_total_cost()
    #     print(order_x)

    # elif currState == 'change_crust':
    #     print(pizza_x)
    
    # #get input  
    # print('CURR_STATE:{}'.format(currState),'\t','PizzaBot:',output_reel[currState])
    # in_value = input().lower().strip()
    # if in_value == 'repeat':
    #     continue
    
    # #cancel order
    # if in_value == 'cancel':
    #     print('Thank you, goodbye!')
    #     break
    
    # ######### additional regex #########
    # if currState == 'add_name':
    #     in_value = re.sub('[^0-9]','',in_value)
    #     #this ensures proper phone format
    #     while len(in_value) != 10:
    #         print('Please enter a 10-digit phone number.')
    #         in_value = input().strip()
    #         in_value = re.sub('[^0-9]','',in_value) 
    #     order_x.set_phone(in_value)
    #     in_value = 'phone_num'
        
    # elif currState == 'delivery_type':
    #     order_x.set_order_name(in_value)
    #     in_value = 'name_val'

    # elif currState == "get_address":
    #     order_x.set_address(in_value)
    #     in_value = "address"

    # elif currState == 'change_crust':
    #     in_value = re.sub('[^\w]','',in_value)
        
    # elif (currState == 'add_phone') or (currState == 'misunderstood_pizza'):
    #     yes_or_no = in_value[0]
    #     if yes_or_no == 'y':
    #         in_value = 'yes_regex'
    #     elif yes_or_no == 'n':
    #         in_value = 'no_regex'

    
    # ########## reset the state ##########
    # try:
    #     currState = state_machine[currState][in_value]
    #     if currState == 'add_pizza':
    #         pizza_x.set_type_of_pizza(in_value)
    #     elif currState == 'change_size':
    #         pizza_x.set_size_of_pizza(in_value)
    #         order_x.add_pizza(pizza_x)
    #     elif currState == 'change_crust':
    #         pizza_x.set_crust_of_pizza(in_value)


    #     if currState == 'confirm_order':
    #         print(output_reel[currState])
            
    # except:
    #     print("Sorry, I didn't get that")