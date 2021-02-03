##################################################
## Homework Assignment #3: "If" Statements
## Element Adder
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Initialising lists
myUniqueList = []
myLeftOvers = []


# Function to check if sent element is already in the myUniqueList
def elementCheck(element):
    for i in range(len(myUniqueList)):
        # Return True is element already exists in the myUniqueList
        if element == myUniqueList[i]:
            return True
        # If indexed element isn't matches with the sent element keep searching
        else:
            continue
    # Return false if element isn't in the myUniqueList
    return False


def addToLeftOvers(element):
    print(element, "already exist in myUniqueList. Adding it to myLeftOvers...")
    myLeftOvers.append(element)


# Function to add element to list
def addElement(element):
    # If sent element is already in the list add that element to myLeftOvers
    if elementCheck(element):
        addToLeftOvers(element)
    # If element doesn't exist in myUniqueList add to it
    else:
        myUniqueList.append(element)


# Adding possible variable types
print("Adding 'Hello' to list... ")
addElement("Hello")
print("Adding 'World' to list... ")
addElement("World")
print("Adding 1 to list... ")
addElement(1)
print("Adding 2.5 to list... ")
addElement(2.5)
print("Adding [5, 7] to list... ")
addElement([5, 7])
print("\n")

# Printing the lists
print("Printing myUniqueList = ", myUniqueList)
print("Printing myLeftOvers = ", myLeftOvers)
print("\n")

# Checking if elementCheck() function and adding to myLeftOvers work
print("Adding 'Hello' to list... ")
addElement("Hello")
print("Adding 'World' to list... ")
addElement("World")
print("Adding 1 to list... ")
addElement(1)
print("Adding 2.5 to list... ")
addElement(2.5)
print("Adding [5, 7] to list... ")
addElement([5, 7])
print("\n")

# Printing the lists
print("Printing myUniqueList = ", myUniqueList)
print("Printing myLeftOvers = ", myLeftOvers)
print("\n")
