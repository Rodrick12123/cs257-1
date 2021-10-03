#This is code by Lysander Miller and Thea Traw

import argparse
import booksdatasource
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function--put in your search term here')
    parser.add_argument('--titles', '-t', nargs='+', help='sort by titles')
    parser.add_argument('--authors', '-a',nargs='+',  help='sort by authors')
    parser.add_argument('--years', '-y',nargs='+', help='sort by years')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    initializedBooksDataSource = booksdatasource.BooksDataSource("books1.csv")
    arguments = get_parsed_arguments()
    if (arguments.authors != None):
        for author in arguments.authors:
            listOfAuthors = initializedBooksDataSource.authors(author)
            for authorObj in listOfAuthors:
                print(authorObj.surname, authorObj.given_name)
    if (arguments.titles != None):
        sortedByYear = False
        for title in arguments.titles:
            if (title == 'year'):
                sortedByYear = True
            elif (title == 'title'):
                pass
            else:
                if (sortedByYear == True):
                    listOfBooks = initializedBooksDataSource.books(title, 'year')
                else:
                    listOfBooks = initializedBooksDataSource.books(title, 'title')
                for book in listOfBooks:
                    print(book.title)
    if (arguments.years != None):
        if (len(arguments.years) > 2):
            print("You've entered too many arguments")
        else:
            listOfBooks = initializedBooksDataSource.books_between_years(arguments.years[0], arguments.years[1])
            for book in listOfBooks:
                print(book.title)

if __name__ == '__main__':
    main()
