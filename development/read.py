# creates a list with the content of the text file
def get_item_list():
    file = open("equipments.txt", "r")
    info = file.readlines()
    file.close()
    return info