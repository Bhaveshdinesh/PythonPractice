number = input("Enter Number: ")
if int(number) % 4 == 0:
    print(number + ', number is multiple of 4')
elif int(number) % 2 == 0:
    print(number + ", is Even number")
else:
    print(number + ", is odd number")