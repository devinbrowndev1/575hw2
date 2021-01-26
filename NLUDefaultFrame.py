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

        if "yes" == in_string or "Yes" == in_string:
            returned_info.append(("yes", "yes"))
        elif "no" == in_string or "No" == in_string:
            returned_info.append(("no", "no"))

        return returned_info

