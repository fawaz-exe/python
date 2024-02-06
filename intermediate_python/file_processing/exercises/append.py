#Question
# Read and Append (E)
# Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.

#Answer
with open('bear1.txt','r') as file1:
    content = file1.read()

with open('bear2.txt', 'a+') as file2:
    file2.write(content)