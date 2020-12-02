"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt):
#     # Your code here
#     txt_lower = txt.lower()
#     return txt_lower.count('x') == txt_lower.count('o')

# without python special things
def XO(txt):
    # lowercase our txt
    txt_lower = txt.lower()
    # sets variable to 0 1st
    x_count = 0
    o_count = 0
    # loop over each character and count X and O
    for char in txt_lower:
        # do something
        # check if char is X or O
        if char == 'x':
            # increment the variable in check
            x_count += 1
        elif char == 'o':
            o_count += 1
    # this will return true or false depending if they equal each other
    return x_count == o_count
        

print(XO('ooxx')) # True
print(XO('xooxx')) # False
print(XO('ooxXm')) # True
print(XO('zzoo')) # False
print(XO('zpzpzpp')) # True

