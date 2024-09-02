from math import exp

def future_discrete_value(x, r, n):
    return x*(1+r)**n

def presemt_discrete_value(x, r, n):
    return x*(1+r)**-n

def future_continuous_value(x, r, t):
    return x*exp(r*t)

def presemt_continuous_value(x, r, t):
    return x*exp(-r*t)

if __name__ == '__main__':
    # value of investment
    x = 100
    # interest rate
    r = 0.071
    # duration
    n = 5
    # value in the future to get the value of investment
    x_future = 142
    print("Future discrete value: ", future_discrete_value(x, r, n))
    print("Present discrete value: ", presemt_discrete_value(x_future, r, n))
    print("Future continuous value: ", future_continuous_value(x, r, n))
    print("Present continuous value: ", presemt_continuous_value(x_future, r, n))
