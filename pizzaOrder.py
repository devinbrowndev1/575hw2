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