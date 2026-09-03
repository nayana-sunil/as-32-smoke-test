class discount_calculator:
    def ApplyDiscount(self, price, percent):
        return price - (price * percent / 100)
