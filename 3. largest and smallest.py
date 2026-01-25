number1 = []
number = []
while number != "":
    number = input("enter a number: ")
    number1.append(number)
    smallest = min(number)
    largest = max(number)
    print("The smallest number is " + smallest)