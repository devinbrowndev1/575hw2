import re

class NLU:
    def __init__(self):
        self.placeholder = ''

    def parse(self,in_state,in_string):
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
        
        return in_value,next_state
