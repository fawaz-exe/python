# #Question
# The existing content of data.txt looks like this:

# 1.3, 1.5

# 2.3, 2.7

# Use Python to modify the content of data.txt so that its content looks like below:

# 1.3, 1.5

# 2.3, 2.7

# 1.3, 1.5

# 2.3, 2.7

# 1.3, 1.5

# 2.3, 2.7

# So, you need to find a way to insert the existing content two more times.

#Answer

with open('data.txt','a+') as datafile:
    datafile.seek(0)
    content = datafile.read()
    datafile.write(content)
    datafile.seek(0)
    datafile.write(content)
