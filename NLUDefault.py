class NLU:
    def __init__(self):
        self.placeholder = ''

    def parse(self,in_state,in_string,in_order,in_pizza):
        if in_state.state_name == 'add_phone':
            in_value = re.sub('[^0-9]','',in_string)
            while len(in_value) != 10:
                print('Please enter a 10-digit phone number.')
                in_value = input().strip()
                in_value = re.sub('[^0-9]','',in_value) 
                
            #SET THE PHONE NUMBER ON THE ORDER
            formatted_in_str = 'phone_num'
            
            index_of_next_state = in_state.possible_input.index(formatted_in_str)
            next_state =  in_state.next_states[index_of_next_state]
        return in_value,next_state
