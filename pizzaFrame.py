#pizza class
class pizzaFrame:
    def __init__(self):
        self.completed = [0,0,0]
        self.type_of_pizza = ''
        self.size_of_pizza = ''
        self.crust_of_pizza = ''
        self.cost_of_pizza = 0
        self.prices = {"type":{"hawaiian": 6, "vegan": 8, "meat lovers":12.5, "4 cheese":6, "pepperoni":4, "veggie supreme":9.5},
                       "size":{"small":{"thin":10, "regular":10, "deep-dish":12, "gluten-free":15},
                               "medium":{"thin":12, "regular":12, "deep-dish":14, "gluten-free":18},
                               "large":{"thin":14, "regular":14, "deep-dish":18, "gluten-free":21}}}
    
    def __str__(self):
        return '''We added a {} {} pizza with {} crust. That will be ${}'''.format(self.size_of_pizza,self.type_of_pizza,self.crust_of_pizza,self.cost_of_pizza)
        
    def set_pizza_info(self, info_type, info_value):

        if info_type == "add_pizza" or info_type == 0:
            self.set_type_of_pizza(info_value)
            self.completed[0] = 1

        elif info_type == "change_size" or info_type == 1:
            self.set_size_of_pizza(info_value)
            self.completed[1] = 1
            
        elif info_type == "change_crust" or info_type == 2:
            self.set_crust_of_pizza(info_value)
            self.completed[2] = 1

    def get_pizza_info(self, info_type):
        if info_type == "add_pizza" or info_type == 0:
            return self.type_of_pizza

        elif info_type == "change_size" or info_type == 1:
            return self.size_of_pizza

        elif info_type == "change_crust" or info_type == 2:
            return self.crust_of_pizza

    def set_type_of_pizza(self,x):
        self.type_of_pizza = x
        self.cost_of_pizza += self.prices["type"][x]
        self.completed[0] = 1

    def set_size_of_pizza(self,x):
        self.size_of_pizza = x
        self.completed[1] = 1
        
    def set_crust_of_pizza(self,x):
        self.crust_of_pizza = x
        self.cost_of_pizza += self.prices["size"][self.size_of_pizza][x]
        self.completed[2] = 1