temps = [223,334,556,453.-999]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

new_temps = [temp / 10 for temp in temps if temp != -999]
print(new_temps)

# Question
# Only Numbers (E)
# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].

# Answer
def foo(mylist):
    newlist = [i for i in mylist if isinstance(i,int)]
    return newlist

#Question 2
##
# Zeros Instead (E)
# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].
##

#Answer

def foo(mylist):
    new_list = [i if not isinstance(i,str) else 0 for i in mylist]
    return new_list

# Question 3
# Convert and Sum Up (E)
# Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers. For example, I called your function with foo(['1.2', '2.6', '3.3']) it should return 7.1. Note that the floats of the input list are string datatypes.

#Answer

def foo(lst):
    return sum([float(i)  if isinstance(i,str) else 0 for i in lst])