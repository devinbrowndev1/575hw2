import sys
import re
import nltk
from state import state
from pizzaOrder import pizzaOrder
from pizza import pizza


state_building_list = [
["start","Welcome to the pizza ordering system.\nPizzaBot:To cancel at anytime type: cancel, To repeat order at anytime type: repeat\nPizzaBot:What specialty pizza would you like?","hawaiian:add_pizza","vegan:add_pizza"]
,["add_pizza","What size? (small,medium,large)","large:change_size","medium:change_size","small:change_size"]
,["change_size","What type of crust? (thin,deepdish,gluten-free)""regular:change_crust","thin:change_crust","deepdish:change_crust","gluten-free:change_crust"]
,["change_crust","Pick-up or delivery?","delivery:get_address","pickup:delivery_type"]
,["get_address","What is your address?","address:delivery_type"]
,["delivery_type","Can I get a name for the order?","name_val:add_name"]
,["add_name","Phone number?","phone_num:add_phone"]
,["add_phone","Got your order. Is above okay? (Y/N)","yes_regex:confirm_order","no_regex:misunderstood_pizza"]
,["misunderstood_pizza","I'm sorry, here's what you asked for ___. Should we restart this pizza?","yes_regex:start","no_regex:confirm_order"]]



#list of built states
fsm = []
for s in state_building_list:
    temp = state()
    temp.build_state(s)
    fsm.append(temp)



#initialize pizzaOrder and pizza
order_x = pizzaOrder()
pizza_x = pizza()




currState = 'start'
while currState != 'confirm_order':

    in_value = input().lower().strip()

    NLU_output = NLU.parses(in_value)

    currState = fsm[NLU_output]

    #all of this goes into regex


    if currState == 'add_phone':
        print('PizzaBot: Here is your order:')
        order_x.set_cost_of_pizzas()
        order_x.set_total_cost()
        print(order_x)

    elif currState == 'change_crust':
        print(pizza_x)
    
    #get input  
    print('CURR_STATE:{}'.format(currState),'\t','PizzaBot:',output_reel[currState])
    in_value = input().lower().strip()
    if in_value == 'repeat':
        continue
    
    #cancel order
    if in_value == 'cancel':
        print('Thank you, goodbye!')
        break
    
    ######### additional regex #########
    if currState == 'add_name':
        in_value = re.sub('[^0-9]','',in_value)
        #this ensures proper phone format
        while len(in_value) != 10:
            print('Please enter a 10-digit phone number.')
            in_value = input().strip()
            in_value = re.sub('[^0-9]','',in_value) 
        order_x.set_phone(in_value)
        in_value = 'phone_num'
        
    elif currState == 'delivery_type':
        order_x.set_order_name(in_value)
        in_value = 'name_val'

    elif currState == "get_address":
        order_x.set_address(in_value)
        in_value = "address"

    elif currState == 'change_crust':
        in_value = re.sub('[^\w]','',in_value)
        
    elif (currState == 'add_phone') or (currState == 'misunderstood_pizza'):
        yes_or_no = in_value[0]
        if yes_or_no == 'y':
            in_value = 'yes_regex'
        elif yes_or_no == 'n':
            in_value = 'no_regex'

    
    ########## reset the state ##########
    try:
        currState = state_machine[currState][in_value]
        if currState == 'add_pizza':
            pizza_x.set_type_of_pizza(in_value)
        elif currState == 'change_size':
            pizza_x.set_size_of_pizza(in_value)
            order_x.add_pizza(pizza_x)
        elif currState == 'change_crust':
            pizza_x.set_crust_of_pizza(in_value)


        if currState == 'confirm_order':
            print(output_reel[currState])
            
    except:
        print("Sorry, I didn't get that")