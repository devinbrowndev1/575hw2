import sys
import re
import nltk


class state:
    def __init__(self):
        self.state_name = ''
        self.possible_input = []
        self.next_states = []
        self.sys_out = []
        
    def __str__(self):
        return "STATE:{}\n SYS_OUT:{}\nPoss. Input:{}\n Next States:{}".format(self.state_name,self.sys_out,self.possible_input,self.next_states)
        
    def build_state(self,state_list):
        self.state_name = state_list.pop(0)
        self.sys_out = state_list.pop(0)
        while len(state_list) > 0:
            in_trans = state_list.pop().split(':')
            self.possible_input.append(in_trans[0])
            self.next_states.append(in_trans[1])

#testing state class
# test = ["start",
# "Welcome to the pizza ordering system.\nPizzaBot:To cancel at anytime type: cancel, To repeat order at anytime type: repeat\nPizzaBot:What specialty pizza would you like?",
# "hawaiian:add_pizza",
# "vegan:add_pizza"]

# s = state()
# s.build_state(test)
# print(s)


#order class
class pizzaOrder:
    def __init__(self):
        self.list_of_pizzas = []
        self.cost_of_pizzas = []
        self.total_cost = 0
        self.order_name = ''
        self.delivery = False
        self.address = ''
        self.phone = ''

    def __str__(self):
        pizz = self.list_of_pizzas[0]
        return '''Got your order for a {} {} pizza on {} crust, which will cost ${}'''.format(pizz.type_of_pizza,
                                                                                             pizz.size_of_pizza,
                                                                                             pizz.crust_of_pizza,
                                                                                             self.total_cost)
    #setter functions
    def add_pizza(self, pizza_obj):
        self.list_of_pizzas.append(pizza_obj)

    def set_cost_of_pizzas(self):
        self.cost_of_pizzas = [c.cost_of_pizza for c in self.list_of_pizzas]

    def set_total_cost(self):
        self.total_cost = sum(self.cost_of_pizzas)

    def set_order_name(self, x):
        self.order_name = x

    def set_delivery(self, x):
        self.delivery(x)

    def set_address(self, x):
        self.address = x

    def set_phone(self, x):
        self.phone = x


#pizza class
class pizza:
    def __init__(self):
        self.type_of_pizza = ''
        self.size_of_pizza = ''
        self.crust_of_pizza = ''
        self.cost_of_pizza = 0
        self.prices = {"type":{"hawaiian": 6, "vegan": 8},
                       "size":{"small":{"thin":10, "regular":10, "deepdish":12, "gluten-free":15}, 
                               "medium":{"thin":12, "regular":12, "deepdish":14, "gluten-free":18}, 
                               "large":{"thin":14, "regular":14, "deepdish":18, "gluten-free":21}}}
    
    def __str__(self):
        return '''We added a {} {} pizza with {} crust. That will be ${}'''.format(self.size_of_pizza,self.type_of_pizza,self.crust_of_pizza,self.cost_of_pizza)
        
    def set_type_of_pizza(self,x):
        self.type_of_pizza = x
        self.cost_of_pizza += self.prices["type"][x]

    def set_size_of_pizza(self,x):
        self.size_of_pizza = x
        
    def set_crust_of_pizza(self,x):
        self.crust_of_pizza = x
        self.cost_of_pizza += self.prices["size"][self.size_of_pizza][x]
        
        
        
#key 1 = current state
#key 2 = input_val
#returns next state
state_machine = {"start": {"hawaiian":"add_pizza","vegan":"add_pizza"},
                 "add_pizza": {"large":"change_size","medium":"change_size","small":"change_size"},
                 "change_size": {"regular":"change_crust","thin":"change_crust","deepdish":"change_crust","gluten-free":"change_crust"},
                 "change_crust": {"delivery":"get_address","pickup":"delivery_type"},
                 "get_address": {"address":"delivery_type"},
                 "delivery_type": {"name_val":"add_name"},
                 "add_name": {"phone_num":"add_phone"},
                 "add_phone": {"yes_regex":"confirm_order","no_regex":"misunderstood_pizza"},
                 "misunderstood_pizza":{"yes_regex":"start","no_regex":"confirm_order"},
                }

#this is for NLG
output_reel = {"start":"Welcome to the pizza ordering system.\nPizzaBot:To cancel at anytime type: cancel, To repeat order at anytime type: repeat\nPizzaBot:What specialty pizza would you like?",
                 "add_pizza":"What size? (small, medium, large)" ,
                 "change_size":"What type of crust? (thin,deepdish,gluten-free)" ,
                 "change_crust":"Pick-up or delivery?" ,
                 "get_address" : "What is your address?",
                 "delivery_type": "Can I get a name for the order?",
                 "add_name":"Phone number?" ,
                 "add_phone":"Got your order. Is above okay? (Y/N)",
                 "confirm_order":"Your order has been received. It will be delivered in 30 minutes or less.",
                 "misunderstood_pizza":"I'm sorry, here's what you asked for ___. Should we restart this pizza?"
                }

order_x = pizzaOrder()
pizza_x = pizza()

currState = 'start'
while currState != 'confirm_order':
    
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