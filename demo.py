# p = Principle Amount
# T = Time Period
# R = Rate of interest per annum

# (p x t x r) / 100

p = float(input('Enter the Principle Amount :- '))
t = float(input('Enter the no of year :- '))
r = float(input('Enter the rate of interest :- '))

si = (p * t * r)/100

print("Simple Interest = ", si)