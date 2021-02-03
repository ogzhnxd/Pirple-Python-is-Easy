##################################################
## Homework #5: Basic Loops
## FizzBuzz and Prime
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Function to check if number is prime
def isPrime(num):
    # Returning False if number is "1"
    if num == 1:
        return False

    # Checking is number is prime
    for i in range(2, num):
        # If number is divisible with any number other than itself returning false
        if num % i == 0:
            return False
        # If number isn't divisible with "i" keep trying other numbers
        else:
            continue
    # If number wasn't divisible with none of the "i"s that mean it's a prime number returning true
    return True


def fizzBuzz(n):
    # Checking numbers from "0" to n
    for i in range(1, n + 1):
        # If number is divisible with both 3 and 5 print "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # If number is divisible with 3 but not with 5 print "Fizz"
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        # If number is divisible with 5 but not with 3 print "Fizz"
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        # If number is prime print "Prime"
        elif isPrime(i):
            print("Prime")
        # If none of conditions isn't met print the number itself
        else:
            print(i)


# Testing with numbers from "1" to "100" (including "100")
fizzBuzz(100)
