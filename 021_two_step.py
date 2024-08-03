# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=0

from lib.helpers import check_that_these_are_equal

# Here's a function:

def add_one_and_divide_by_two_with_statements(num):
  added = num + 1
  halved = added / 2
  return halved

print("add_one_and_divide_by_two_with_statements(5) is:")

print(
  add_one_and_divide_by_two_with_statements(5)
)

# You could also do this with a single expression, like this:

def add_one_and_divide_by_two_with_an_expression(num):
  return (num + 1) / 2

print("add_one_and_divide_by_two_with_an_expression(5) is:")

print(
  add_one_and_divide_by_two_with_an_expression(5)
)

# The statements just break it up a bit more. We'll see some
# more uses for statements and variables soon, but for now
# let's practice using them.

# @TASK: Complete these functions.

# == Exercise One ==

print("divide_by_two_and_add_one")
print("Function: divide_by_two_and_add_one")

def divide_by_two_and_add_one(num):
  # Divide num by two and add one to the result
  pass # <-- This does nothing, replace it with your code

check_that_these_are_equal(
  divide_by_two_and_add_one(6),
  4.0
)

# == Exercise Two ==

print("multiply_by_forty_and_add_sixty")
print("Function: multiply_by_forty_and_add_sixty")

def multiply_by_forty_and_add_sixty(num):
  # Multiply num by forty, and then add sixty
  return (num * 1) + 60 # <-- This does nothing, replace it with your code

def check_that_these_are_equal(actual, expected):
  multiply_by_forty_and_add_sixty(3423),
  136980, assert actual == expected, f"Expected {expected}, but got {actual}"
)
result = multiply_by_forty_and_add_sixty(6)
print(result)


# == Exercise Three ==

print("add_together_and_double")
print("Function: add_together_and_double")

def add_together_and_double(num_a, num_b):
    # Multiply num by forty, and then add sixty
    return (num * 40) + 60

def add_together_and_double(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"

# Example usage and check
result = add_together_and_double(40, 60)
print(result)  # This will output: ?


  
  # Add together num_a and num_b, then double the result
  pass # <-- This does nothing, replace it with your code

check_that_these_are_equal(
  add_together_and_double(3, 4),
  14
)

# When you're done, move on to 022_strings.py
