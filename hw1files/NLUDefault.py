from SemanticFrame import SemanticFrame
import re

class NLUDefault:

    def __init__(self):
        self.SemanticFrame = SemanticFrame()

        self.oflavors = ["vegan", "hawaiian", "meat lovers", "4 cheese", "pepperoni", "veggie supreme"]
        self.osizes = ["small", "medium", "large"]
        self.ocrusts = ["thin", "regular", "gluten-free", "deep-dish"]
        self.onames = ["Jessica", "Devin", "Alex", "Alexandra"]
        self.oaddresses = ["195 Stevens Way", "185 Stevens Way", "155 Stevens Way"]

    def parse(self, inputStr):
        self.SemanticFrame.Domain = "pizza"

        flavors = self.oflavors
        sizes = self.osizes
        crusts = self.ocrusts
        names = self.onames
        addresses = self.oaddresses

        for flavor in flavors:
            if flavor in inputStr.lower():
                self.SemanticFrame.Intent = "INFORM"
                self.SemanticFrame.Slots["pizza_type"] = flavor
        for size in sizes:
            if size in inputStr.lower():
                self.SemanticFrame.Intent = "INFORM"
                self.SemanticFrame.Slots["pizza_size"] = size
        for crust in crusts:
            check_format = re.sub("-", "", crust)
            if crust in inputStr.lower() or check_format in inputStr.lower():
                self.SemanticFrame.Intent = "INFORM"
                self.SemanticFrame.Slots["pizza_crust"] = crust
        for name in names:
            if name in inputStr or name.lower() in inputStr:
                self.SemanticFrame.Intent = "INFORM"
                self.SemanticFrame.Slots["order_name"] = name

        for address in addresses:
            if address in inputStr:
                self.SemanticFrame.Intent = "INFORM"
                self.SemanticFrame.Slots["order_address"] = address

        if "delivery" in inputStr.lower():
            self.SemanticFrame.Intent = "INFORM"
            self.SemanticFrame.Slots["order_delivery"] = "delivery"
        elif "pickup" in inputStr.lower() or "pick-up" in inputStr.lower():
            self.SemanticFrame.Intent = "INFORM"
            self.SemanticFrame.Slots["order_delivery"] = "pick-up"

        if "reorder" in inputStr.lower():
            self.SemanticFrame.Intent = "REORDER"

        if "1234567890" in inputStr:
            self.SemanticFrame.Intent = "INFORM"
            self.SemanticFrame.Slots["order_phone"] = "1234567890"

        if "yes" == inputStr or "Yes" == inputStr:
            self.SemanticFrame.Intent = "CONFIRM"
        elif "no" == inputStr or "No" == inputStr:
            self.SemanticFrame.Intent = "DENY"

        return self.SemanticFrame
