########################################################################
## Homework Assignment #1: Variables
## My Favorite Music as a Dictionary and Guessing the Attributes of It
########################################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
########################################################################

# Function to check is user guess is correct or not
def guessingGame(key, value):
    # If given key and key value is correct returning True
    if key in myFavoriteMusic and myFavoriteMusic[key] == value:
        return True
    # Returning False in all other cases
    else:
        return False


# myFavoriteMusic from Homework 1 as dictionary
myFavoriteMusic = {"musicName": "K/DA - DRUM GO DUM ft. Aluna, Wolftyla, Bekuh BOOM (Official Audio)",
                   "album": "K/DA ALL OUT",
                   "musicGroup": "K/DA",
                   "groupMembers": "Ahri, Akali, Evelynn, Kai'Sa",
                   "featuring": "Aluna, Wolftyla, Bekuh BOOM",
                   "genre": "K-POP",
                   "durationInSeconds": 200,
                   "producer": "Riot Music Team",
                   "releaseDate": "6 November 2020",
                   "platforms": "Spotify, Youtube Music, Apple Music, Deezer ,Amazon Music",
                   "musicYoutubeLink": "https://www.youtube.com/watch?v=VLE6Y1q13qE",
                   "viewsOnYoutube": 6243685,
                   "likes": 215128,
                   "dislikes": 2598,
                   "likeToDislikeRatio": 98.8,
                   }

# Infinite Loop for guessing game
while True:

    # Printing keys in myFavoriteMusic
    for attribute in myFavoriteMusic:
        print(attribute)

    # Getting input from user for key and key value
    guessKey = input("Which attribute you want to guess ? You can choose from above : ")
    guessKeyValue = input("What is your guess ? ")

    # If key exist in myFavoriteMusic and key value is correct congratulate user
    if guessingGame(guessKey, guessKeyValue):
        print("Congratulations !!! You guess was correct")
    # Else inform user
    else:
        print("Sorry your guess wasn't correct :(")

    # Ask user if he/she wants to play again
    playAgain = input("Do you want to play again ? (Y/N) : ")

    # If yes continue
    if playAgain == "Y":
        continue
    # If no exit from loop
    elif playAgain == "N":
        break

# Lastly print all keys and key values of myFavoriteMusic
for attribute in myFavoriteMusic:
    print("{} : {}".format(attribute, myFavoriteMusic[attribute]))
