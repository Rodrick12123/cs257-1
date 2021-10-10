#This is code by Lysander Miller and Thea Traw

import argparse
import booksdatasource
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function--put in your search terms here')
    parser.add_argument('--titles', '-t', nargs='*',default='NoData', help='sort by titles')
    parser.add_argument('--authors', '-a',nargs='*',default='NoData',  help='sort by authors')
    parser.add_argument('--years', '-y',nargs='*',default='NoData', help='sort by years')
    parser.add_argument('--moreHelp', '-mh', '-mH', nargs='*', default = 'NoData', help='provides more information on search')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    initializedBooksDataSource = booksdatasource.BooksDataSource("books1.csv")
    arguments = get_parsed_arguments()
    listOfAuthors = []
    listOfAuthorsAlreadyPrinted = []
    if (arguments.moreHelp != 'NoData'):
        file = open('usage.txt', 'r')
        contents = file.read()
        print(contents)
    if (arguments.authors != 'NoData'):
        handle_author_call()
    if (arguments.titles != 'NoData'):
        handle_title_call()
    if (arguments.years != 'NoData'):
        handle_years_call()
                
def handle_title_call():
    sortedByYear = False
    listOfBooks = []
    index = 0
    if ((len(arguments.titles) == 0)):
        listOfBooks = initializedBooksDataSource.books(None, 'title')
    else:
        for title in arguments.titles:
            if (title == 'year'):
                sortedByYear = True
                index +=1
            elif (title == 'title'):
                index +=1
                pass
            else:
                if (sortedByYear == True):
                    listOfBooks += initializedBooksDataSource.books(title, 'year')
                else:
                    listOfBooks += initializedBooksDataSource.books(title, 'title')
                if ((len(arguments.titles)) == index):
                    if (sortedByYear == True):
                        listOfBooks = initializedBooksDataSource.books(None, 'year')
                    else:
                        listOfBooks = initializedBooksDataSource.books(None, 'title')
            if (sortedByYear == False):
                listOfBooks = sorted(listOfBooks, key=lambda x: (x.title))
            else:
                listOfBooks = sorted(listOfBooks, key=lambda x: (x.publication_year, x.title))
        listOfBooksAlreadyPrinted = []
        for book in listOfBooks:
            if (book not in listOfBooksAlreadyPrinted):
                print(book.title)
                listOfBooksAlreadyPrinted.append(book)
    
def handle_author_call():
    if ((len(arguments.authors)) > 0):
            for author in arguments.authors:
                listOfAuthors += initializedBooksDataSource.authors(author)
        elif ((len(arguments.authors)) == 0):
            listOfAuthors = initializedBooksDataSource.authors(None)
        listOfAuthors = sorted(listOfAuthors, key=lambda x: (x.surname, x.given_name))
        for authorObj in listOfAuthors:
            if ((authorObj in listOfAuthorsAlreadyPrinted) == False):
                print(authorObj.surname+", "+authorObj.given_name)
                listOfAuthorsAlreadyPrinted.append(authorObj)
    
def handle_years_call():
    if (len(arguments.years) == 0):
            listOfBooks = initializedBooksDataSource.books_between_years(None, None)
            for book in listOfBooks:
                print(book.title)
        elif (len(arguments.years) > 2):
            print("You've entered too many arguments")
        else:
            if (len(arguments.years) == 1):
                listOfBooks = initializedBooksDataSource.books_between_years(arguments.years[0], None)
            elif (arguments.years[0].lower() == 'none' and arguments.years[1].lower() != 'none'):
                listOfBooks = initializedBooksDataSource.books_between_years(None, arguments.years[1])
            elif (arguments.years[1].lower() == 'none' and arguments.years[0].lower() != 'none'):
                listOfBooks = initializedBooksDataSource.books_between_years(arguments.years[0], None)
            elif (arguments.years[0].lower() == 'none' and arguments.years[1].lower() == 'none'):
                listOfBooks = initializedBooksDataSource.books_between_years(None, None)
            else:
                listOfBooks = initializedBooksDataSource.books_between_years(arguments.years[0], arguments.years[1])
            for book in listOfBooks:
                print(book.title)
    

if __name__ == '__main__':
    main()
