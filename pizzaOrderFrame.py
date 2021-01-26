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
        self.list_of_pizzas.append(pizza_obj)
        self.completed[0] = 1

    def set_order_info(self, info_type, info_value):
        if info_type == "add_name":
            self.order_name = info_value
            self.completed[1] = 1

        elif info_type == "delivery_type":
            if info_value == "delivery":
                self.delivery = True
                self.completed[2] = 1
            else:
                self.delivery = False
                self.completed[2] = 1
                self.completed[3] = 1

        elif info_type == "add_address":
            self.address = info_value
            self.completed[3] = 1

        elif info_type == "add_phone":
            self.phone = info_value
            self.completed[4] = 1


    def set_cost_of_pizzas(self):
        self.cost_of_pizzas = [c.cost_of_pizza for c in self.list_of_pizzas]

    def set_total_cost(self):
        self.total_cost = sum(self.cost_of_pizzas)

    def set_order_name(self, x):
        self.order_name = x
        self.completed[1] = 1

    def set_address(self, x):
        self.address = x
        self.completed[3] = 1

    def set_phone(self, x):
        self.phone = x
        self.completed[4] = 1