#This is code by Lysander Miller and Thea Traw

import argparse
import booksdatasource
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function--put in your search term here')
    parser.add_argument('--titles', '-t', nargs='+', help='sort by titles')
    parser.add_argument('--titles year', '-t year', nargs='+', help='sort by titles')
    parser.add_argument('--titles title', '-t title', nargs='+', help='sort by titles')
    parser.add_argument('--authors', '-a',nargs='+',  help='sort by authors')
    parser.add_argument('--years', '-y',nargs='+', help='sort by years')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    initializedBooksDataSource = booksdatasource.BooksDataSource("books1.csv")
    arguments = get_parsed_arguments()
    if (arguments.titles != None): 
        for title in arguments.titles:
            listOfBooks = initializedBooksDataSource.books(title, 'title')
            for book in listOfBooks:
                print(book.title)
    if (arguments.titles year != None):
        for title in arguments.titles year:
            listOfBooks = initializedBooksDataSource.books(title, 'year')
            for book in listOfBooks:
                print(book.title)
    if (arguments.titles title != None):
        for title in argument.titles title:
            listOfBooks = initializedBooksDataSource.books(title)
            for book in listOfBooks:
                print(book.title)
    alreadyPrintedAuthors =[]
    if (arguments.authors != None):
        for author in arguments.authors:
            if (author == "N"):
                listOfAuthorsNone = initializedBooksDataSource.authors(None)
                for noneAuthor in listOfAuthorsNone:
                    print(noneAuthor.surname, noneAuthor.given_name)
            else:
                listOfAuthorsWithString = initializedBooksDataSource.authors(author)
                for authorWithString in listOfAuthorsWithString:
                    if ((authorWithString in alreadyPrintedAuthors) == False):
                        print(authorWithString.surname, authorWithString.given_name)
                        alreadyPrintedAuthors.append(authorWithString)
    #if (len(arguments.years) > 2):
        #print("")
       #print(arguments.years)
    #else:
        #print("")
        #print(booksdatasource.BooksDataSource.books_between_years(arguments.years[0], arguments.years[1]))

if __name__ == '__main__':
    main()
