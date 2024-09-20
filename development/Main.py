import operations

print("\n")
print("\t\t\t\t\t\t\t\t\tWelcome to 711 Rentals")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\tKamalpokhari, Kathmandu | Phone No: 9803423822")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")

loop = True
while loop == True:
    operations.options()
    error = False
    while error == False:
        try:
            user_input = input("Choose the option you want:")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            error = True
        except:
            user_input = int(input(" Enter a valid response."))

    if user_input == '1':
        operations.rentProduct()

    if user_input == '2':
        operations.returnProduct()

    if user_input == '3':
        print("Thank you for visiting our store.")
        loop = False
