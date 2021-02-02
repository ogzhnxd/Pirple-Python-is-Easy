##################################################
## Homework Assignment #3: "If" Statements
## Equality Checker
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

def isEqual(var1, var2, var3):
    # Type casting to integer values if a string value is sent
    var1 = int(var1)
    var2 = int(var2)
    var3 = int(var3)

    # Checking if there is a equality between values
    if var1 == var2 or var2 == var3 or var1 == var3:
        # Returning True if there is at least 2 values equal to each other
        return True

    else:
        # Returning False if none of the values are equal to each other
        return False


# Sending parameters to function and printing the returned value
print(isEqual("1", 1, "3"))
