import operations
import read

# creates the bill for the rent function.
def rent_bill(rent_list, total_amount):
    item_list = read.get_item_list()
    main_info = operations.get_table(item_list)
    name = input("Enter your name:")
    print("=" * 194)
    date = operations.get_date()
    time = operations.get_time()
    

    error = False
    while error == False:
        try:
            contact = input("Enter your contact Number")
            error = True
        except:
            print("=" * 194)
            contact = input("Enter a valid contact number")
    file = open(name + "_rent" + ".txt", "w")
    file.write("                           711 Rentals invoice                                    ")
    file.write("_" * 90 + "\n")
    file.write("{:<80}{:<80}".format("Name:", name) + "\n")
    file.write("Contact:" + contact + "\n")
    file.write("_" * 90 + "\n")
    file.write("{:<80}{:<80}".format("Date:" + date, "Time:" + time + "\n"))
    file.write("_" * 90 + "\n")
    file.write("{:<20}{:<20}{:<20}{:<20}{:<20}".format("item", "Brand", "Quantity", "Price", "Amount")+"\n")
    file.write("\n" + "*" * 90 + "\n")

    for i in range(len(rent_list)):
        rented_id = int(rent_list[i][0])
        rented_quantity = int(rent_list[i][1])
        item_name = main_info[rented_id][0]
        item_brand = main_info[rented_id][1]
        item_price = main_info[rented_id][2]
        amount = int(main_info[rented_id][2].replace("$", "")) * rented_quantity
        file.write("{:<20}{:<20}{:<20}{:<20}{:<20}".format(item_name, item_brand, rented_quantity, item_price, str(amount)))

    file.write("\n" + "_" * 90 + "\n")
    
    total = total_amount
    file.write("_" * 90 + "\n")
    file.write("Total Amount:                                                                   $" + str(total) + "\n")
    file.write("*" * 90)
    file.close()

    print("_" * 90)
    print("{:<80}{:<80}".format("Name :" + name, "Receipt"))
    print("Contact:" + contact)
    print("_" * 90)
    print("{:<80}{:<80}".format("Date:" + date, "Time:" + time))
    print("_" * 90)
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("item", "Brand", "Quantity", "Price", "Amount"))
    print()
    print("=" * 90)
    for i in range(len(rent_list)):
        rented_id = int(rent_list[i][0])
        rented_quantity = int(rent_list[i][1])
        item_name = main_info[rented_id][0]
        item_brand = main_info[rented_id][1]
        item_price = main_info[rented_id][2]
        amount = int(main_info[rented_id][2].replace("$", "")) * rented_quantity
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(item_name, item_brand, rented_quantity, item_price, "$" + str(amount)))
    print("\n" + "_" * 90)
    
    total_amount = total_amount
    print("_" * 90)
    print("Total Amount:                                                                   $" + str(total_amount))

    print("_" * 90)
    print("\n")
    print("What would you like to do next?")

    # creates bill for the return
def return_bill(rent_list, total_amount):
    item_list = read.get_item_list()
    main_info = operations.get_table(item_list)
    rentDays=int(input("Enter the number of days you rented: "))
    fineday=0
    fine_amount=0
    if rentDays<1:
        raise ValueError
    else:
        if rentDays<=5:
            fine_amount=0
        elif rentDays%5!=0:
            fineday=(int(rentDays//5)+1)*5
            fine_amount=int((fineday/5))*int(total_amount)
        else:
            fine_amount=(rentDays-5)*int(total_amount)
    name = input("Enter your name:")
    print("=" * 194)
    date = operations.get_date()
    time = operations.get_time()

    error = False
    while error == False:
        try:
            contact = input("Enter your contact Number:")
            error = True
        except:
            print("=" * 194)
            contact = input("Enter a valid contact number:")
    file = open(name + "_return" + ".txt", "w")
    file.write("_" * 90 + "\n")
    file.write("{:<80}{:<80}".format("Name:" + name, "Receipt")+'\n')
    file.write("Contact:" + contact + "\n")
    file.write("_" * 90 + "\n")
    file.write("{:<80}{:<80}".format("Date:" + date, "Time:" + time + "\n"))
    file.write("_" * 90 + "\n")
    file.write("{:<20}{:<20}{:<20}{:<20}{:<20}".format("item", "Brand", "Quantity", "Price", "Amount") +"\n")
    file.write("\n" + "=" * 90 + "\n")

    for i in range(len(rent_list)):
        rented_id = int(rent_list[i][0])
        rented_quantity = int(rent_list[i][1])
        item_name = main_info[rented_id][0]
        item_brand = main_info[rented_id][1]
        item_price = main_info[rented_id][2]
        amount = int(main_info[rented_id][2].replace("$", "")) * rented_quantity
        file.write( "{:<20}{:<20}{:<20}{:<20}{:<20}".format(item_name, item_brand, rented_quantity, item_price,str(amount))+"\n")

    file.write("\n" + "_" * 90 + "\n")
    file.write("fine Amount:                                                                     $" + str(fine_amount) + "\n")
    total = fine_amount + total_amount
    file.write("_" * 90 + "\n")
    file.write("Total Amount:                                                                   $" + str(total) + "\n")
    file.write("*" * 90)
    file.close()

    print("_" * 90)
    print("{:<80}{:<80}".format("Name :" + name, "Receipt"))
    print("Contact:" + contact)
    print("_" * 90)
    print("{:<80}{:<80}".format("Date:" + date, "Time:" + time))
    print("_" * 90)
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("item", "Brand", "Quantity", "Price", "Amount"))
    print("=" * 90)
    for i in range(len(rent_list)):
        rented_id = int(rent_list[i][0])
        rented_quantity = int(rent_list[i][1])
        item_name = main_info[rented_id][0]
        item_brand = main_info[rented_id][1]
        item_price = main_info[rented_id][2]
        amount = int(main_info[rented_id][2].replace("$", "")) * rented_quantity
        print(
            "{:<20}{:<20}{:<20}{:<20}{:<20}".format(item_name, item_brand, rented_quantity, item_price,"$" + str(amount)))
    print("\n" + "_" * 90)
    print("{:<80}{:<80}".format("fine Amount:", "$" + str(fine_amount)))
    total_amount = fine_amount + total_amount 
    print("_" * 90)
    print("Total Amount:                                                                   $" + str(total_amount))

    print("_" * 90)
    print("\n")
    print("What would you like to do next?")