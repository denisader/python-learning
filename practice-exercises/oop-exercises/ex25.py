class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = Cart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("mango")

print("Number of items in cart:", len(cart))