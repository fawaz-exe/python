user_input = input('Enter Your Name: ')
# message = "Hello %s" % user_input
message = f"Hello {user_input}" # this method is better imo
print(message)

name = input('Enter Your Name: ')
Surname = input('Enter your surname: ')

output = "Hello %s %s" % (name, Surname)
output = f'Hello {name} {Surname} !'
print(output)

# More String Formatting
# There is also another way to format strings using the "{}".format(variable) form. Here is an example:

# name = "John"
# surname = "Smith"
 
# message = "Your name is {}. Your surname is {}".format(name, surname)
# print(message)
# Output: Your name is John. Your surname is Smith

# Question

Formatting and Uppercase
# Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). Note that the first letter of the person's name should always be uppercase.

def foo(name):
    
    output = f"Hi {name}".title()
    return output

foo("john")