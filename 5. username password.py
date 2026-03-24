username = "python"
password = "rules"
input1 = input("\nplease enter your username: ")
input2 = input("please enter your password: ")
attempts = 0
if input1 == username and input2 == password:
    print("\nWelcome")
else:
    while attempts < 4:     #as long as there is attempt left
        input1 = input("\nplease enter your username again: ")
        input2 = input("please enter your password again: ")
        attempts = attempts + 1
    print("\nAccess Denied")