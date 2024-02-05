monday = [9.1,3.23,45.5]

for temperature in monday:
    print(round(temperature))

#     Loop Over Integer Colors (E)
# Loop over the colors items and print out the item in every loop only if the item is an integer. So, the output of your program would be:

# 11
# 43
# 54
# 54
    
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for items in colors:
    if items == int(items):
        print(items)