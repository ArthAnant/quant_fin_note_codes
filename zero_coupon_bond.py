class zero_coupon_pricing:
    def __init__(self, principal, maturity, market_rate):
        self.principal = principal
        self.maturity = maturity
        self.market_rate = market_rate / 100

    def present_value(self, x, n):      
        # x is value at maturity and n is maturity duration in years, present value returns the amount the investor pays for the bond
        return x / (1+self.market_rate)**n

    def calcuate_value(self): #this is just a helper function to implement the present_value formula
        return self.present_value(self.principal, self.maturity)
    
if __name__ == '__main__':
    #an investor buys a zero coupon bond priced at 1000 for 2 years and wishes to get a 4% return, this will calculate the discounted price the investor should pay to make the desired return
    bond_price = zero_coupon_pricing(1000, 2, 4)    
    print("%.2f" % bond_price.calcuate_value())