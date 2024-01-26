# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Pseudocode

# Indicate the values
number1 = 20
number2 = 30
number3 = 40
number4 = 30

# Check if the values for given 1 is less than or equal to 1000
if number1 * number2 <= 1000:
# Return if the condition is true
    result = number1 * number2
else:
# If the values are over 1000, sum it  
    result = number1 + number2
# Print the result for 1st given
print("The result is", result)

# Check if the values for given 2 is less than or equal to 1000  
if number3 * number4 <= 1000:
# Return if the condition is true
    result = number3 * number4
else:
# If the values are over 1000, sum it
    result = number3 + number4
# Print the result for 2nd given
print("The result is", result)
