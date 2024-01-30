''' This program was created by 
Maria Luisa Freitas de Lucena and
Raquel de Melo Teófilo
'''

from webScraping import *
import os

# List of options 
OPTIONS = [
    "All categories of books",
    "Save books into json file",
    "Check prices",
    "Check books that start with the letter A",
    "Check rating",
    "Statistics",
    "Exit Program"
]

# Clears screen 
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Prints each option of the list options
def showOptions(OPTIONS):
    print("OPTIONS:")
    i = 1
    for item in OPTIONS:
        print("({}) {}".format(i,item))
        i+=1

# Prompts an integer input from the user   
def getIntegerInput(input_msg, min_value, max_value):
    while True:
        try:
            user_input = int(input(input_msg))
        except(ValueError, TypeError):
            print("ERROR! Please insert a number")
        else: 
            if user_input < min_value or user_input > max_value:
                print("ERROR! Option doesn't exist")
            else:
                return user_input

# Gets the user option and returns it  
def getUserOption():
    showOptions(OPTIONS)
    option = getIntegerInput("Choose an option: ",1,len(OPTIONS))
    return option

# Handle user chosen option 
def handleUserOption():
    while True:
        clearScreen()
        chosen_option = getUserOption()
        if chosen_option == 1:
            clearScreen()
            getCategories()
            input("\n(Press enter to go back)")
        elif chosen_option == 2:
            clearScreen()
            saveBooks()
            input("\n(Press enter to go back)")
        elif chosen_option == 3:
            clearScreen()
            printBooks(getSpecificPrices())
            input("\n(Press enter to go back)")
        elif chosen_option == 4:
            clearScreen()
            printBooks(getBooksLetterA())
            input("\n(Press enter to go back)")
        elif chosen_option == 5:
            clearScreen()
            getSpecificRating()
            input("\n(Press enter to go back)")
        elif chosen_option == 6:
            clearScreen()
            printStatistics()
            totalBooks()
            totalBooksByRating()
            totalBooksByPriceUnder10()
            totalBooksByPriceOver10()
            totalBooksByPriceUnder25()
            totalBooksByPriceOver25()
            totalBooksByPriceUnder50()
            totalBooksByPriceOver50()
            input("\n(Press enter to go back)")
        else:
            clearScreen()
            print("Exiting program...")
            return

# Initialize function
handleUserOption()