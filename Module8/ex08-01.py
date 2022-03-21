"""
Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list
that contains all but the first and last e lements.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


def chop(lst):
    """
    Takes a list, modifies it, removing the first and last elements, and
    returns None.
    Input:  lst -- a list
    Output: None
"""
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element


def middle(lst):
    """
    Takes a list and returns a new list that contains all but the first and
    last elements.
    Input: lst -- a list
    Output: new -- new list with first and last elements removed
    """
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

print("\n\n\n\n\nBefore function calls: my_list", my_list)
print("Before function calls: my_list2", my_list2,"\n\n")

print("Calling 'chop_list'...\n")
chop_list = chop(my_list)
print("After first chop call: ", my_list)                       # Should be [2,3]
print("Returned value of 'chop_list' function: ", chop_list,"\n\n") # Should be None

print("Calling 'middle_list'...\n")
middle_list = middle(my_list2)
print("original list was unchanged: ", my_list2)                        # Should be unchanged
print("Type of value returned: ", type(my_list2))
print("Values that were returned by the function call: ",middle_list)                      # Should be [2,3]


print("\n\n\n\n\nAfter function calls: my_list", my_list)
print("After: my_list2 after function calls", my_list2)
