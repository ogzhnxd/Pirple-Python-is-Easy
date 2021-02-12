##################################################
## Homework Assignment #8: I/O
## Note Taker
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
#################################################################################################################
## Important Note : For program to work correctly you should extract the file from zip and then run the program
#################################################################################################################

# Importing os to check if a file exist in some directory
import os

# Getting the directory that program is in and printing it
path = os.getcwd()
print(path)

# Opening an example file and writing some things in for testing purposes
file = open("xd.txt", "w")
file.write("lol\n")
file.write("lmao\n")
file.write("xd\n")
file.close()

# Getting filename from user
filename = input("Enter your file name including '.txt' : ")

# Checking if file exists in program directory
# If file exists ask user what to do with file
if os.path.isfile(path + "\\" + filename):
    print("That file is already exists.")
    option = input("What do you want to do with {} file ? (Enter 'r' to read, 'd' to delete and start over, 'a' to append, 'wl' to change a certain line.) : ")

    # If user selects "r" option read file
    if option == "r":
        # Open the file in read mode
        file = open(filename, "r")
        # Read and print the contents of the file
        print(file.read())

        # Finally close the file
        file.close()

    # If user selects "d" option;
    elif option == "d":
        #  Remove the file and open a new one in write mode
        os.remove(filename)
        file = open(filename, "w")

        # Ask user what to write in file
        text = input("What do you want write in {} file ? ".format(filename))

        # Write the user input to file
        file.write(text)
        print("Your text has been written to the file.")

        # Finally close the file
        file.close()

    # If user selects "a" option;
    elif option == 'a':
        # Open the file in append mode
        file = open(filename, "a")

        # Ask user what to append
        text = input("What do you want append into {} file ? ".format(filename))

        # Appent user input to the file
        file.write(text)
        print("Your text has been added to the file.")

        # Finally close the file
        file.close()

    # If user selects "wl" option;
    else:
        # Open the file in read mode
        file = open(filename, "r")

        # Ask user which line to change and with which text
        lineIdx = int(input("Which line do you want to change ? "))
        lineText = input("What do you want to write into that line ?")

        lines = []
        # Read lines of the file and append it into a list
        for line in file:
            lines.append(line)

        # Change the desired line's content
        lines[lineIdx-1] = lineText + "\n"

        # Close the file
        file.close()

        # Open the file in write mode to overwrite everthing
        file = open(filename, "w")

        # Write the new content
        file.writelines(lines)

        # Finally close the file
        file.close()

# If file doesn't exists in program directory
else:
    # Ask user what to write into file
    text = input("What do you want write in {} file ? ".format(filename))

    # Open a new file
    file = open(filename, "w")

    # Write user input into it
    file.write(text)
    print("Your text has been written to the file.")

    # Finally close the file
    file.close()
