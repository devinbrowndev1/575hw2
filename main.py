from pizzaOrderFrame import pizzaOrderFrame
from pizzaFrame import pizzaFrame
from NLUDefaultFrame import NLU


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

pizza_slot_request = ["What can I do for you?",
                      "What size pizza would you like?",
                      "What crust do you want on your pizza?"]

pizza_reorder_request = ["Do you want a {} pizza?",
                      "Do you want a {} pizza",
                      "Do you want {} crust?"]

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
            break

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

    slot_list = parser.parse(in_value)

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
                if confirmed_order_info == 0:
                    order_x.add_pizza(pizza_compare)
                elif confirmed_order_info == 1:
                    order_x.set_order_name(order_compare.order_name)
                elif confirmed_order_info == 2:
                    order_x.delivery = order_compare.delivery
                    order_x.completed[2] = 1
                elif confirmed_order_info == 3:
                    order_x.set_address(order_compare.address)
                elif confirmed_order_info == 4:
                    order_x.set_phone(order_compare.phone)
            elif confirmed_pizza_info >= 0:
                if confirmed_pizza_info == 0:
                    pizza_x.set_type_of_pizza(pizza_compare.type_of_pizza)
                elif confirmed_pizza_info == 1:
                    pizza_x.set_size_of_pizza(pizza_compare.size_of_pizza)
                elif confirmed_pizza_info == 2:
                    pizza_x.set_crust_of_pizza(pizza_compare.crust_of_pizza)
        elif info_type == "no":
            print("Okay, we'll ignore your stored order information.")
            reorder = False

        if info_type in pizza_values:
            pizza_x.set_pizza_info(info_type, value)
        else:
            order_x.set_order_info(info_type, value)

    print(pizza_x)
    try:
        print(order_x)
    except:
        print("")


print("Thanks for your order!")
