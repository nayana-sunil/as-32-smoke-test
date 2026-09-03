class order_service:
    def calculateTotal(self, items):
        try:
            return sum(item.price for item in items)
        except:
            return 0
