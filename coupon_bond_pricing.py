class coupon_bond:
    def __init__(self, principal, coupon_rate, maturity, market_rate):
        self.principal = principal
        self.coupon_rate = coupon_rate / 100
        self.maturity = maturity
        self.market_rate = market_rate / 100

    def present_value(self, x, n):
        return x/(1 + self.market_rate)**n
    
    def calculate_price(self):
        price = 0
        # Coupon payments
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal * self.coupon_rate, t)
            

        # Present value of principal
        price = price + self.present_value(self.principal, self.maturity)

        return price
    
if __name__=='__main__':
    couponBond = coupon_bond(1000, 10, 3, 4)
    print(couponBond.calculate_price())