class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        
        if self.discount == 0:
            print("There is no discount to apply.")
            return "There is no discount to apply."

        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        self.total = round(self.total)  
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            if isinstance(last_item, tuple):
                last_price = last_item[1] * last_item[2]  # Calculate total price for multiple items
            else:
                last_price = last_item

            try:
                last_price = float(last_price)  # Convert the total price to float
            except ValueError:
                print("Error: Unable to convert price to float.")
                return

            self.total -= last_price