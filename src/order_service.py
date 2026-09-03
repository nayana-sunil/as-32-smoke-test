class order_service:
    def calculateTotal(self, items):
        self.TotalAmount = 0
        self.taxRate = 0.08
        try:
            for item in items:
                self.TotalAmount += item.price
            return self.TotalAmount * (1 + self.taxRate)
        except:
            return 0
