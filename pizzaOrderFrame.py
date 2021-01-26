class pizzaOrderFrame:
    def __init__(self):
        self.completed = [0,0,0,0,0]
        self.list_of_pizzas = []
        self.order_name = ''
        self.delivery = False
        self.address = ''
        self.phone = ''
        self.cost_of_pizzas = []
        self.total_cost = 0
        self.wait_time = 20


    def __str__(self):
        pizz = self.list_of_pizzas[0]
        if self.delivery:
            return '''Got your order for a {} {} pizza on {} crust, which will cost ${}. The name for the order is {} and it will be delivered to {}'''.format(pizz.size_of_pizza,pizz.type_of_pizza,pizz.crust_of_pizza,self.total_cost,self.order_name, self.address)  
        else:
            return '''Got your order for a {} {} pizza on {} crust, which will cost ${}. The name for the order is {} and it scheduled for pickup.'''.format(pizz.size_of_pizza,pizz.type_of_pizza,pizz.crust_of_pizza,self.total_cost,self.order_name)  

    #setter functions
    def add_pizza(self, pizza_obj):
        if len(self.list_of_pizzas) == 0:
            self.list_of_pizzas.append(pizza_obj)
        else:
            self.list_of_pizzas[0] = pizza_obj
        self.completed[0] = 1

    def set_order_info(self, info_type, info_value):
        if info_type == "add_pizza" or info_type == 0:
            self.add_pizza(info_value)
        elif info_type == "add_name" or info_type == 1:
            self.order_name = info_value
            self.completed[1] = 1

        elif info_type == "delivery_type" or info_type == 2:
            if info_value == True:
                self.delivery = True
                self.completed[2] = 1
            else:
                self.delivery = False
                self.completed[2] = 1
                self.completed[3] = 1

        elif info_type == "add_address" or info_type == 3:
            self.address = info_value
            self.completed[3] = 1

        elif info_type == "add_phone" or info_type == 4:
            self.phone = info_value
            self.completed[4] = 1

    def get_order_info(self, info_type):
        if info_type == "add_pizza" or info_type == 0:
            return self.list_of_pizzas[0]

        elif info_type == "add_name" or info_type == 1:
            return self.order_name

        elif info_type == "delivery_type" or info_type == 2:
            return self.delivery

        elif info_type == "add_address" or info_type == 3:
            return self.address

        elif info_type == "add_phone" or info_type == 4:
            return self.phone
        else:
            return None

    def set_total_cost(self):
        self.total_cost = sum(self.cost_of_pizzas)

