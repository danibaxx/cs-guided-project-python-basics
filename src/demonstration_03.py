"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Your code here
    return (int(txt))

print(type(string_int("3")))
# isinstance will check the value passed to what you are turning it into
print(isinstance(string_int("3"), int))
