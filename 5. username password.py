username = "python"
password = "rules"
attempts = 5                                       #total attempts
while attempts > 0:                                #as long as there is attempt left
    input1 = input("\nplease enter your username: ")
    input2 = input("please enter your password: ")
    if username == input1 and password == input2:
        print("\nWelcome")
        break                                       #otherwise the program will ask for username again
    else:
        attempts = attempts - 1
        print(f"\n You have {attempts} attempts left")   #tells left attempts
else:                                                    #if the attempt is equal to 0
    print("\nAccess Denied")