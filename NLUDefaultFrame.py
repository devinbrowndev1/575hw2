import re

class NLU:
    def __init__(self):
        self.placeholder = ''

    def parse(self,in_string):

        numbers = re.compile("[0-9]")

        returned_info = []

        flavors = ["vegan", "hawaiian"]
        sizes = ["small", "medium", "large"]
        crusts = ["thin", "regular", "gluten-free", "deep-dish"]
        names = ["Jessica", "Devin", "Alex", "Alexandra"]
        addresses = ["195 Stevens Way", "185 Stevens Way", "155 Stevens Way"]

        for flavor in flavors:
            if flavor in in_string:
                returned_info.append((flavor, "add_pizza"))
        for size in sizes:
            if size in in_string:
                returned_info.append((size, "change_size"))
        for crust in crusts:
            if crust in in_string:
                returned_info.append((crust, "change_crust"))
        for name in names:
            if name in in_string:
                returned_info.append((name, "add_name"))

        if "delivery" in in_string:
            returned_info.append(("delivery", "delivery_type"))
        elif "pickup" in in_string or "pick-up" in in_string:
            returned_info.append(("pickup", "delivery_type"))

        if "reorder" in in_string:
            returned_info.append(("reorder", "reorder"))

        if any(map(str.isdigit, in_string)):
            in_value = re.sub('[^0-9]', '', in_string)
            if len(in_value) == 10:
                returned_info.append((in_value, "add_phone"))
            else:
                returned_info.append(("123 Main Street", "add_address"))

        return returned_info

    """
        if in_state.state_name == "add_pizza" or in_state.state_name == "change_size":
            in_value = in_string
            next_state = in_state.get_next_state(in_value)

        elif in_state.state_name == 'add_phone':
            in_value = re.sub('[^0-9]','',in_string)
            while len(in_value) != 10:
                print('Please enter a 10-digit phone number.')
                in_value = input().strip()
                in_value = re.sub('[^0-9]','',in_value) 
                
            formatted_in_str = 'phone_num'
            next_state = in_state.get_next_state(formatted_in_str)

        elif in_state.state_name == 'add_name':
            in_value = in_string
            formatted_in_str = 'name_val'
            next_state =  in_state.get_next_state(formatted_in_str)
            
        elif in_state.state_name == "change_crust":
            in_value = in_string
            formatted_in_str = re.sub('[^\w]','',in_value)
            if formatted_in_str in ['gf','glutenfree','glutenf']:
                formatted_in_str = 'glutenfree'
            elif formatted_in_str in ['reg','regular','regl','normal']:
                formatted_in_str = 'regular'
            elif formatted_in_str in ['deepdish','dd','deep']:
                formatted_in_str = 'deepdish'
            elif formatted_in_str in ['thin','th','skinny']:
                formatted_in_str = 'thin'

            next_state = in_state.get_next_state(formatted_in_str)

        elif in_state.state_name == "delivery_type":
            if in_string != "delivery":
                in_value = "pickup"
            else:
                in_value = "delivery"

            next_state = in_state.get_next_state(in_value)
            
        elif in_state.state_name == 'get_address':
            in_value = in_string
            formatted_in_str = 'address'
            next_state =  in_state.get_next_state(formatted_in_str)

        elif (in_state.state_name == 'check_order') or (in_state.state_name == 'misunderstood_pizza'):
            in_value = in_string
            yes_or_no = in_value[0]
            if yes_or_no == 'y':
                in_value = 'yes_regex'
            elif yes_or_no == 'n':
                in_value = 'no_regex'
            next_state = in_state.get_next_state(in_value)

        return in_value,next_state"""
