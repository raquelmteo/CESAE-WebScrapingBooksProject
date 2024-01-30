''' This program was created by 
Maria Luisa Freitas de Lucena and
Raquel de Melo Teófilo
'''

from bs4 import BeautifulSoup
import requests
import json

# List of all books 
listAllBooks = []
listAllRatings = []

# Locators
CATEGORIESLOCATOR = "div.side_categories ul li a"
BOOKLOCATOR = "article.product_pod"
COVERLOCATOR = "img.thumbnail"
RATINGLOCATOR = "p.star-rating"
TITLELOCATOR = "h3 a"
PRICELOCATOR = "div.product_price p.price_color"
NEXTPAGELOCATOR = "ul.pager li"

# Selects all book categories and returns in a list
def getCategories():
    categories = [element.get_text(strip=True) for element in soup.select(CATEGORIESLOCATOR)] #uses strip and to get only the content without tags and white spaces
    printsCategories(categories)

def printsCategories(categories):
    print("CATEGORIES:\n")
    for category in categories:
        print(category)
    
# Selects all books and returns it
def getAllBooks():
    return soup.select(BOOKLOCATOR)

# Selects the cover of the book and returns it
def getCover(book):
    cover_link = book.select_one(COVERLOCATOR).attrs['src']
    # Concatenates to get the full link
    full_link = "https://books.toscrape.com" + cover_link.replace(".","",2)
    return full_link

# Maches the rating name with a number and returns it
def getRatingNumeric(rating):
    match rating:
        case 'One':
            return 1
        case 'Two':
            return 2
        case 'Three':
            return 3
        case 'Four':
            return 4
        case 'Five':
            return 5

# Selects the rating of the book and returns as numeric
def getRating(book):
    rating = book.select_one(RATINGLOCATOR).attrs['class']
    numeric_rating = getRatingNumeric(rating[1])
    return numeric_rating

# Selects the title of the book and returns it
def getTitle(book):
    title = book.select_one(TITLELOCATOR).attrs['title']
    return title

# Selects the price of the book and returns as a float
def getPrice(book):
    price = book.select_one(PRICELOCATOR).text
    price = float(price[1:])
    return price

# Extracts informations of a book and returns into dictionary
def extractBookInfo(book):
    cover = getCover(book)
    rating = getRating(book)
    title = getTitle(book)
    price = getPrice(book)
    return {
        'cover' : cover,
        'rating' : rating,
        'title' : title,
        'price' : price
    }

# Uses function to extract information of each book and adds to list
def extractAllDataFromBooks(books):
    for book in books:
        listAllBooks.append(extractBookInfo(book))

# Prints each information of the book
def printBook(book):
    print(f"""
Cover: {book['cover']}\n
Rating: {book['rating'] }\n
Title: {book['title']}\n
Price: {book['price']}
    """)

# Prints all books from a list
def printBooks(listBooks):
    print("\nAll books:")
    if listBooks:
        for book in listBooks:
            printBook(book)
    else:
        print("\nNão foram encontrados resultados")

# Selects the maximum number of pages of the website
def getMaxPage():
    page = requests.get(f'https://books.toscrape.com')
    soup = BeautifulSoup(page.content, 'html.parser')
    page = soup.select_one(NEXTPAGELOCATOR).get_text(strip=True)
    return int(page[-2:])

# Saves page content into json file
def saveBooks():
    try:
        with open("ficheiro.json","w") as f:
            json.dump(listAllBooks,f,indent=4) 
    except:
        print("\nError: Something went wrong")
    else:
        print("File created with success!")

# Select books between specific prices
def getSpecificPrices():
    while True:
        try:
            min_price = float(input("Insert the minimum price: ")) 
            break
        except ValueError:
            print("Invalid input, please enter a valid rating.")
    while True:
        try:
            max_price = float(input("Insert the maximum price: ")) 
            if max_price > min_price:
                priceFilter = [book for book in listAllBooks if min_price <= book['price'] <= max_price]
                return priceFilter
            else:
                print("Please insert a price higher than the minimum.")
        except ValueError:
            print("Invalid input, please enter a valid rating.")

# Selects books with A as first letter 
def getBooksLetterA():
    letterFilter = [book for book in listAllBooks if book['title'].startswith('A')]
    return letterFilter

# Select books between specific ratings 
def getSpecificRating():
    while True:
        try:
            rating = int(input("Insert a rating (1-5): "))
            if 1 <= rating <= 5:
                ratingFilter = [book for book in listAllBooks if book['rating'] == rating]
                printBooks(ratingFilter)
                break
            else:
                print("Please insert a rating between 1 and 5.")
        except ValueError:
            print("Invalid input, please enter a valid rating.")

# Prints staststics 
def printStatistics():
    print("STASTISTICS OF THE BOOKS\n")

# Prints the total books
def totalBooks():
    totalBooks = len(listAllBooks)
    print(f"Total: {totalBooks}")

# Gets all ratings and puts into list
def getAllRatings():
    for book in listAllBooks:
        listAllRatings.append(book['rating'])
    return listAllRatings

# Prints the total books by rating
def totalBooksByRating():
    ratings = getAllRatings()
    print(f"With rating 1: {ratings.count(1)}")
    print(f"With rating 2: {ratings.count(2)}")
    print(f"With rating 3: {ratings.count(3)}")
    print(f"With rating 4: {ratings.count(4)}")
    print(f"With rating 5: {ratings.count(5)}")

# Counts books priced under or equals 10
def totalBooksByPriceUnder10():
    booksPrice = len([book for book in listAllBooks if  book['price'] <= 10])
    print(f"Under or equal £10.00: {booksPrice}")

# Counts books priced over 10
def totalBooksByPriceOver10():
    booksPrice = len([book for book in listAllBooks if  book['price'] > 10])
    print(f"Over £10.00: {booksPrice}")

# Counts books under or equals 25
def totalBooksByPriceUnder25():
    booksPrice = len([book for book in listAllBooks if  book['price'] <=25 ])
    print(f"Under or equal £25.00: {booksPrice}")

# Counts books priced over 25
def totalBooksByPriceOver25():
    booksPrice = len([book for book in listAllBooks if  book['price'] >25 ])
    print(f"Over £25.00: {booksPrice}")

# Counts books priced under or equals 50
def totalBooksByPriceUnder50():
    booksPrice = len([book for book in listAllBooks if  book['price'] <=50 ])
    print(f"Under or equal £50.00: {booksPrice}")

# Counts books priced over 50
def totalBooksByPriceOver50():
    booksPrice = len([book for book in listAllBooks if  book['price'] >50 ])
    print(f"Over £50.00: {booksPrice}")

# Extracts data of each page of the website 
for i in range(1,getMaxPage()):
    if i == 1:
        page = requests.get(f'https://books.toscrape.com/index.html')
    else:
        page = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    # Creates list with all books
    allBooks = getAllBooks()
    # Extracts all data from all books
    extractAllDataFromBooks(allBooks)