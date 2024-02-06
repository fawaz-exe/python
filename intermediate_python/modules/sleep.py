import time

while True:
    with open('fruits.txt','r') as file:
        print(file.read())
        time.sleep(10)
