class order_service:
    def calculateTotal(self, items):
        self.TotalAmount = 0
        try:
            for item in items:
                self.TotalAmount += item.price
            return self.TotalAmount
        except:
            return 0
