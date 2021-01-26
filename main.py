from pizzaOrderFrame import pizzaOrderFrame
from pizzaFrame import pizzaFrame
from NLUDefaultFrame import NLU


canceled_order = False

#setup example pizza
pizza_example = pizzaFrame()
pizza_example.type_of_pizza = 'vegan'
pizza_example.size_of_pizza = 'small'
pizza_example.crust_of_pizza = 'regular'
pizza_example.cost_of_pizza = 10
pizza_example.completed = [1,1,1]

#set up example order
order_example = pizzaOrderFrame()
order_example.list_of_pizzas = [pizza_example]
order_example.order_name = 'Jessica'
order_example.total_cost = 10
order_example.phone = '1234567890'
order_example.address = '123 Way'
order_example.delivery = True
order_example.completed = [1,1,1,1,1]

account_dict = {
    '1234567890':order_example
}

pizza_slot_request = ["What would you like?",
                      "What size pizza would you like?",
                      "What crust do you want on your pizza?"]

pizza_reorder_request = ["Do you still want a {} pizza?",
                      "Do you still want a {} pizza",
                      "Do you still want {} crust?"]

order_slot_request = ["What kind of pizza do you want?",
                      "What is your name?",
                      "Do you want pickup or delivery?",
                      "What is your address?",
                      "What is your phone number?"]

order_reorder_request = ["Do you still want this pizza?:\n{}",
                      "Is your name {}?",
                      "This is for {}, right?",
                      "Is your address still {}?",
                      "And your phone number is still {}?"]


#initialize pizzaOrder and pizza
order_x = pizzaOrderFrame()
pizza_x = pizzaFrame()
parser = NLU()

orderIncomplete = True
pizza_values = ["add_pizza", "change_size", "change_crust"]
pizza_complete = [1,1,1]
order_complete = [1,1,1,1,1]

reorder = False
confirmed_pizza_info = -1
confirmed_order_info = -1

while orderIncomplete:
    if (pizza_x.completed == pizza_complete):
        order_x.add_pizza(pizza_x)
        if order_x.completed == order_complete:
            orderIncomplete = False
            print(order_x)
            print('Is this correct? (yes/no)')
            yno = input()
            confirm_list = parser.parse(yno)
            if confirm_list[0][0] == 'yes':
                break
            else:
                print('Okay let\'s start over from the beginning.')
                orderIncomplete = True
                order_x = pizzaOrderFrame()
                pizza_x = pizzaFrame()

    asked_for_info = False

    for i, x in enumerate(pizza_x.completed):
        if x == 0 and not asked_for_info:
            if reorder:
                confirmed_pizza_info = i
                if i == 0:
                    print(pizza_reorder_request[i].format(pizza_compare.type_of_pizza))
                elif i == 1:
                    print(pizza_reorder_request[i].format(pizza_compare.size_of_pizza))
                elif i == 2:
                    print(pizza_reorder_request[i].format(pizza_compare.crust_of_pizza))
            else:
                print(pizza_slot_request[i])
            asked_for_info = True

    for i,x in enumerate(order_x.completed):
        if x == 0 and not asked_for_info:
            if reorder:
                confirmed_order_info = i
                if i == 0:
                    print(order_reorder_request[i].format(order_compare.list_of_pizzas[0]))
                elif i == 1:
                    print(order_reorder_request[i].format(order_compare.order_name))
                elif i == 2:
                    if order_compare.delivery == True:
                        print(order_reorder_request[i].format("delivery"))
                    else:
                        print(order_reorder_request[i].format("pick-up"))
                elif i == 3:
                    print(order_reorder_request[i].format(order_compare.address))
                elif i == 4:
                    print(order_reorder_request[i].format(order_compare.phone))
            else:
                print(order_slot_request[i])
            asked_for_info = True

    in_value = input().strip()

    if in_value == 'cancel':
        print('Sorry to see you go! Please come again!')
        canceled_order = True
        break

    slot_list = parser.parse(in_value)
    out_str = ''
    for s in slot_list:
        #print(s[1])
        if s[1] == 'add_name':
            out_str +=  'Name '
        elif s[1] == 'address ':
            out_str += 'Address'
        elif s[1] == 'delivery_type':
            out_str += 'Delivery method '
        elif s[1] == 'add_phone':
            out_str += 'Phone number '
        elif s[1] == 'change_size':
            out_str += 'Pizza size '
        elif s[1] == 'change_crust':
            out_str += 'Pizza crust '
        elif s[1] == 'add_pizza':
            out_str += 'Pizza type'
            
    if len(out_str) > 0:
        print('Okay we got the following information:')
        print(out_str)
        print('-------------------')


    for slot in slot_list:
        value, info_type = slot

        if info_type == 'reorder':
            reorder = True
            print("What is your phone number for the account?")
            account_input = input().lower()
            order_compare = account_dict[account_input]
            pizza_compare = order_compare.list_of_pizzas[0]

        if info_type == "yes":
            if confirmed_order_info >= 0:
                order_x.set_order_info(confirmed_order_info, order_compare.get_order_info(confirmed_order_info))
            else:
                pizza_x.set_pizza_info(confirmed_pizza_info, pizza_compare.get_pizza_info(confirmed_pizza_info))
                order_x.add_pizza(pizza_x)
        elif info_type == "no":
            print("Okay, we'll ignore your stored order information.")
            reorder = False

        if info_type in pizza_values:
            pizza_x.set_pizza_info(info_type, value)
        else:
            order_x.set_order_info(info_type, value)





if not canceled_order:
    print("Thanks for your order! It will be ready in {} minutes.".format(order_x.wait_time))
