import sys
import re
import nltk

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
        return '''List of pizzas:{}
                Cost of pizzas:{}
                Total cost:{}
                Order name:{}
                Delivery:{}
                Addresss:{}
                Phone:{}
                '''.format(self.list_of_pizzas,self.cost_of_pizzas,self.total_cost,self.order_name,
                          self.delivery,self.address,self.phone)
    #setter functions
    def set_list_of_pizzas(self, pizza_obj):
        self.list_of_pizzas.append(pizza_obj)

    def set_cost_of_pizzas(self, cost):
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
                       "size":{"small":{"thin":10, "regular":10, "deep":12, "gf":15}, 
                               "medium":{"thin":12, "regular":12, "deep":14, "gf":18}, 
                               "large":{"thin":14, "regular":14, "deep":18, "gf":21}}}
        
    def set_type_of_pizza(self,x):
        self.type_of_pizza = x
        self.cost_of_pizza += self.prices["type"][x]

    def set_size_of_pizza(self,x):
        self.size_of_pizza = x
        
    def set_crust_of_pizza(self,x):
        self.crust_of_pizza = x
        self.cost_of_pizza += self.prices[self.size_of_pizza][x]

#key 1 = current state
#key 2 = input_val
#returns next state
state_machine = {"start": {"hawaiian":"add_pizza","vegan":"add_pizza"},
                 "add_pizza": {"large":"change_size","medium":"change_size","small":"change_size"},
                 "change_size": {"delivery":"delivery_type","pickup":"delivery_type"},
                 "delivery_type": {"name_val":"add_name"},
                 #we need to make the phone number dynamic
                 "add_name": {"phone_num":"add_phone"},
                 "add_phone": {"yes":"confirm_order"}
                }

#this is for NLG
output_reel = {"start":"Welcome to the pizza ordering system. What pizza would you like?",
                 "add_pizza":"What size? (small, medium, large)" ,
                 "change_size":"Pick-up or delivery?" ,
                 "delivery_type": "Name?",
                 "add_name":"Phone number?" ,
                 "add_phone":"Got your order for a large Hawaiian on regular crust. Is that okay? (Y/N)",
                 "confirm_order":"Your order has been received. It will be delivered in 30 minutes or less and cost $20.00."
                }



order_x = pizzaOrder()
pizza_x = pizza()

currState = 'start'
while currState != 'confirm_order':
    print(output_reel[currState], 'CURR_STATE',currState)
    in_value = input().lower()
    
    #additional regex
    if currState == 'add_name':
        in_value = re.sub('[^0-9]','',in_value)
        order_x.set_phone(in_value)
        in_value = 'phone_num'
    elif currState == 'delivery_type':
        order_x.set_order_name(in_value)
        in_value = 'name_val'
    elif currState == 'change_size':
        in_value = re.sub('[^\w]','',in_value)
    
    #reset the state
    try:
        currState = state_machine[currState][in_value]
        if currState == 'add_pizza':
            pizza_x.set_type_of_pizza(in_value)
        elif currState == 'change_size':
            pizza_x.set_size_of_pizza(in_value)

        if currState == 'confirm_order':
            print(output_reel[currState])
            
    except:
        print("Sorry, I didn't get that")

print(order_x)