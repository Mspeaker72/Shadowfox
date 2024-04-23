# 1. Create a variable named pi and store the value 22/7 in it.
# Now check the data type of this variable.
pi = 22 / 7
print(type(pi))
# The type is a float

# 2. Create a variable called for and assign it a value 4. See what
# happens and find out the reason behind the behavior that you
# see.
four = 4
print(type(four))
# The type is an integer
# // is integer division returns and in while / will return float

# 3. Store the principal amount, rate of interest, and time in
# different variables and then calculate the Simple Interest for 3
# years. Formula: Simple Interest = P x R x T / 100

# Given values
P = 1000  # Principal amount in dollars
R = 10 # Rate of interest (5% in decimal form)
T = 3    # Time in years

# Calculate Simple Interest
simple_interest = (P * R * T)/100

print(f"The Simple Interest for 3 years is: ${simple_interest:.2f}")


