"""
This is a helper function to read file and placing its content into 
a list that is returned.... super pythonic powers - activate!!!!!

Pass file name string and will get a populated list returned.
"""

def getAddys(addressList):

    # addressList = "addressList.txt"
    addyList = []

# this opens and reads file passed from driver function
    with open(addressList) as file:
        addyList = [line.strip() for line in file]

    # print(addyList)
    return addyList


    # file3Handle = open(addressList)
    # for address in file3Handle:
    #     addyList.extend = address

    # print(addyList)
    # for addys in file3Handle:
    #     print (addys)