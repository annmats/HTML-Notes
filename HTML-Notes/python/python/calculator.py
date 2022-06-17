x = float(input ("What's x? "))
y = float(input ("What's y? "))

# Putting two decimal places
z = round (x / y, 2)

# To put separator (,)
print (f"{z:,}")