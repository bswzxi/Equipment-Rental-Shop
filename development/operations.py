import datetime
import read
import write1


def options():
    print("Select any one of these options:")
    print("1. Enter 1 to Rent.")
    print("2. Enter 2 to Return.")
    print("3. Enter 3 to exit.")


# creates a table with all of the items
def get_table(item_list):
    item_table = {}
    for index in range(len(item_list)):
        item_table[index + 1] = item_list[index].replace("\n", "").split(",")
    return item_table


def print_item_table():  # Displays all the  costumes in the data dictionary
    item_list = read.get_item_list()
    main_info = get_table(item_list)
    print("=" * 194)
    print("{:<20}{:<30}{:<30}{:<20}{:<30}".format("ID", "item", "Brand", "Price", "Quantity",))
    print("=" * 194)
    for key, value in main_info.items():
        print("{:<20}{:<30}{:<30}{:<20}{:<30}".format(key, value[0], value[1], value[2], value[3],))
        print("-" * 194)

    print("=" * 194)


# Checks the ID inserted by the user
def check_id():
    item_list = read.get_item_list()
    main_info = get_table(item_list)

    not_available = True
    while not_available == True:
        error = False
        while error == False:
            try:
                checked_id = int(input("Enter the ID of the item you would like to rent."))
                while checked_id <= 0 or checked_id > 5:
                    print("Enter the valid equipment number")
                    checked_id = int(input("Enter the ID of the item you would like to rent."))
                
                error = True
                print()
            except:
                checked_id = int(input("Please enter a valid response."))
            
            if checked_id <= len(main_info) and checked_id > 0:
                if (main_info[checked_id][3] == "0"):
                    print("-" * 194)
                    print("Sorry this item is out of stock.")
                    print("-" * 194)
                    print()
                    not_available = True
                else:
                    print("-" * 194)
                    print("The item is available")
                    print("=" * 194)
                    not_available = False

    return checked_id


# Checks the quantity inserted by the user.
def check_quantity(checked_id):
    item_list = read.get_item_list()
    main_info = get_table(item_list)
    quantity = int((main_info[checked_id][3]))
    validity = False
    while validity == False:
        entered_quantity = int(input("How many items would you like to rent?"))
        if entered_quantity > 0 and entered_quantity <= quantity:

            print("=" * 194)
            print("System has been updated")
            print("=" * 194)
            validity = True

        elif entered_quantity > quantity:
            print("=" * 194)
            print("Not enough items Available.")
        else:
            print("Enter a valid amount.")

    return entered_quantity


# Sets current data as a variable.
def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    date = year + "/" + month + "/" + day
    return date


# Sets the current time as a variable.
def get_time():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    if int(minute) < 10:
        minute = "0" + minute
        time = (hour + ":" + minute)
    else:
        time = (hour + ":" + minute)
    return time



# assigns id according to the brand.
def assign_id(brand):
    valid_brand = False
    while valid_brand == False:
        if brand == "1":
            brand = 1
            valid_brand = True
        elif brand == "2":
            brand = 2
            valid_brand = True
        elif brand == "3":
            brand = 3
            valid_brand = True
        elif brand == "4":
            brand = 4
            valid_brand = True
        elif brand == "5":
            brand = 5
            valid_brand = True
        else:
            brand = input("Enter a valid ID.")
    return brand

# Function for rents option.
def rentProduct():
    total_amount = 0
    rent_list = []
    keep_renting = True
    while keep_renting == True:
        print("#" * 159)
        rent_welcome = "shop 711 Rentals products"
        welcome_rent = rent_welcome.center(177, "*")
        print(welcome_rent)
        print("\n")

        print_item_table()

        checked_id = check_id()
        checked_quantity = check_quantity(checked_id)

        rent_list.append([checked_id, checked_quantity])

        item_list = read.get_item_list()
        main_info = get_table(item_list)

        # to get the price of the items
        amount = int(main_info[checked_id][2].replace("$", "")) * int(checked_quantity)
        total_amount += amount

        main_info[checked_id][3] = str(int(main_info[checked_id][3]) - checked_quantity)

        file = open("equipments.txt", "w")
        for data in main_info.values():
            write = data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "\n"
            file.write(write)
        file.close()
        dont_rent = False
        while dont_rent == False:
            rent = input("Keep renting?(y/n)")
            if rent == "y":
                keep_renting = True
                break

            elif rent == "n":
                write1.rent_bill(rent_list, total_amount)
                keep_renting = False
                dont_rent = True
        else:
            print("Please enter a valid Response.")  


# Funciton for return.
def returnProduct():
    rent_list = []#rentedItems
    keep_renting = True#more
    total_amount = 0
    while keep_renting == True:
        error = False
        while error == False:
            try:
                print_item_table()
                brand = input("Enter the Item ID you need to return.")
                print("="*140)
                error = True
                print()
            except:
                brand = input("Please enter a valid response.")
                print("=" * 140)

            quantity = int(input("How many items would you like to return.?"))
            print("=" * 140)

            item_list = read.get_item_list()
            main_info = get_table(item_list)


            brand = brand.lower()
            brand_id = int(assign_id(brand))

            main_info[brand_id][3] = str(int(main_info[brand_id][3]) + quantity)

            rent_list.append([brand_id, quantity])
            amount = int(main_info[brand_id][2].replace("$", "")) * int(quantity)
            total_amount += amount

            file = open("equipments.txt", "w")
            for data in main_info.values():
                write = data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "\n"
                file.write(write)
            file.close()
            
            #add
            error = False
            while error == False:
                try:
                    ask_rent = input("Would you like to continue returning?(y/n)")
                    error = True
                except:
                    ask_rent = input("Please enter a valid response.")
                if ask_rent == "y":
                    keep_renting = True
                if ask_rent == "n":
                    write1.return_bill(rent_list, total_amount)
                    keep_renting = False



