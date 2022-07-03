class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
        elif is_increased == False:
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"Product's Name: {self.name}")
        print(f"Product's Price: {self.price}")
        print(f"Product's Category: {self.category}")
    
    def get_category(self):
        return self.category