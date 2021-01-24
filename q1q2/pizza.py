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
        
    def set_pizza_info(self, info_type, info_value):
        if info_type == "add_pizza":
            self.set_type_of_pizza(info_value)

        elif info_type == "change_size":
            self.set_size_of_pizza(info_value)
            
        elif info_type == "change_crust":
            self.set_crust_of_pizza(info_value)

    def set_type_of_pizza(self,x):
        self.type_of_pizza = x
        self.cost_of_pizza += self.prices["type"][x]

    def set_size_of_pizza(self,x):
        self.size_of_pizza = x
        
    def set_crust_of_pizza(self,x):
        self.crust_of_pizza = x
        self.cost_of_pizza += self.prices["size"][self.size_of_pizza][x]
        print(self.cost_of_pizza)