class NLU:
    def __init__(self):
        self.placeholder = ''

    def parse(self,in_state,in_string):
        if in_state.state_name == 'add_phone':
            in_value = re.sub('[^0-9]','',in_string)
            while len(in_value) != 10:
                print('Please enter a 10-digit phone number.')
                in_value = input().strip()
                in_value = re.sub('[^0-9]','',in_value) 
                
            formatted_in_str = 'phone_num'
            index_of_next_state = in_state.possible_input.index(formatted_in_str)
            next_state =  in_state.next_states[index_of_next_state]

        elif in_state.state_name == 'add_name':
            in_value = in_string
            formatted_in_str = 'name_val'
            index_of_next_state = in_state.possible_input.index(formatted_in_str)
            next_state =  in_state.next_states[index_of_next_state]
            
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
        
            index_of_next_state = in_state.possible_input.index(formatted_in_str)
            next_state =  in_state.next_states[index_of_next_state]
            
        elif in_state.state_name == 'get_address':
            in_value = in_string
            formatted_in_str = 'address'
            index_of_next_state = in_state.possible_input.index(formatted_in_str)
            next_state =  in_state.next_states[index_of_next_state]
        
        return in_value,next_state
