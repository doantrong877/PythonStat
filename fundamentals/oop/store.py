from product import Product
class Store:
    def __init__(self,name):
        self.list_product = []
        self.name = name
    
    def add_product(self, new_product):
        self.list_product.append(new_product)
        return self

    def sell_product(self, id):
        item = self.list_product[id]
        print(item)
        self.list_product.remove(id)
        return self

    def inflation(self, percent_increase):
        for i in self.list_product:
            self.list_product[i].update_price(percent_increase, True)
        
    def set_clearance(self, category, percent_discount):
        for i in self.list_product:
            if self.list_product[i].get_category() == category:
                self.list_product[i].update_price(percent_discount, False)

    def get_product(self):
        return self.list_product
def test_method():
    amazon = Store("Amazon")
    shirt = Product("shirt", 5.0, "Clothing")
    pants = Product("pants", 10.0, "Clothing")
    hat = Product("hat", 20.0, "Clothing")
    amazon.add_product(shirt).add_product(pants).add_product(hat)

    for i in amazon.get_product():
        i.print_info()

test_method()

