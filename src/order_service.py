class OrderService:
    def calculate_total(self, items):
        return sum(item.price for item in items)
