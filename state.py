class state:
    def __init__(self):
        self.state_name = ''
        self.transitions = {}
        self.sys_out = []
        
    def __str__(self):
        return "STATE:{}\n SYS_OUT:{}\nPoss. Input:{}\n Next States:{}".format(self.state_name,self.sys_out,self.possible_input,self.next_states)
        
    def build_state(self,state_list):
        self.state_name = state_list.pop(0)
        self.sys_out = state_list.pop(0)
        while len(state_list) > 0:
            in_trans = state_list.pop().split(':')
            self.transitions[in_trans[0]] = in_trans[1]

    def get_next_state(self, user_input):
        return self.transitions[user_input].state_name