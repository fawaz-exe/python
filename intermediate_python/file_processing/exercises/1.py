#Question
# Reading and Processing Text (E)
# Read the bear.txt file, and print out the first 90 characters of its content.

#Answer
with open("bear.txt") as myfile:
    content = myfile.read()
    print(content[:90])
    