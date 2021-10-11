#This is code by Lysander Miller and Thea Traw
#Revised by Thea Traw

import argparse
import booksdatasource
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function')
    parser.add_argument('--titles', '-t', nargs='*',default='NoData', help='sort by titles')
    parser.add_argument('--authors', '-a',nargs='*',default='NoData',  help='sort by authors')
    parser.add_argument('--years', '-y',nargs='*',default='NoData', help='sort by years')
    parser.add_argument('--morehelp', '-mh', '-?', nargs='*', default = 'NoData', help='provides more information on search')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    initialized_books_data_source = booksdatasource.BooksDataSource("books1.csv")
    arguments = get_parsed_arguments()
    
    if arguments.morehelp != 'NoData':
        file = open('usage.txt', 'r')
        contents = file.read()
        print(contents)
    if arguments.authors != 'NoData':
        handle_author_call(initialized_books_data_source, arguments)
    if arguments.titles != 'NoData':
        handle_title_call(initialized_books_data_source, arguments)
    if arguments.years != 'NoData':
        handle_years_call(initialized_books_data_source, arguments)
                
def handle_title_call(initialized_books_data_source, arguments):
    
    sorted_by_year = False
    number_of_arguments = 0
    list_of_books = []
    if len(arguments.titles) == 0:
        list_of_books = initialized_books_data_source.books(None)
    else:
        for term in arguments.titles:
            if term == 'year':
                sorted_by_year = True
                number_of_arguments += 1
            elif term == 'title':
                number_of_arguments += 1
                pass
            else:
                
                if sorted_by_year == True:
                    list_of_books += initialized_books_data_source.books(term, 'year')
                else:
                    list_of_books += initialized_books_data_source.books(term, 'title')
                if len(arguments.titles) == number_of_arguments:
                    if sorted_by_year == True:
                        list_of_books = initialized_books_data_source.books(None, 'year')
                    else:
                        list_of_books = initialized_books_data_source.books(None, 'title')
            if sorted_by_year == False:
                list_of_books = sorted(list_of_books, key=lambda x: (x.title))
            else:
                list_of_books = sorted(list_of_books, key=lambda x: (x.publication_year, x.title))
    
    list_of_books_already_printed = []
    for book in list_of_books:
        if (book not in list_of_books_already_printed):
            print(book.title+' ('+book.publication_year+')')
            list_of_books_already_printed.append(book)
    
def handle_author_call(initialized_books_data_source, arguments):
    list_of_authors = []
    list_of_authors_already_printed = []
    
    if len(arguments.authors) > 0:
        for author in arguments.authors:
            list_of_authors += initialized_books_data_source.authors(author)
    elif len(arguments.authors) == 0:
        list_of_authors = initialized_books_data_source.authors(None)
        #list_of_authors = sorted(list_of_authors, key=lambda x: (x.surname, x.given_name))
    for author in list_of_authors:
        if author not in list_of_authors_already_printed:
            print(author.surname+', '+author.given_name)
            for book in initialized_books_data_source.books_by_author(author):
                print("    "+book.title+' ('+book.publication_year+')')
            list_of_authors_already_printed.append(author)
    
def handle_years_call(initialized_books_data_source, arguments):
    
    if len(arguments.years) == 0:
        list_of_books = initialized_books_data_source.books_between_years(None, None)
        #for book in listOfBooks:
            #print(book.title)
    elif len(arguments.years) > 2:
        print("You've entered too many arguments")
    else:
        if len(arguments.years) == 1:
            list_of_books = initialized_books_data_source.books_between_years(arguments.years[0], None)
        elif (arguments.years[0].lower() == 'none' and arguments.years[1].lower() != 'none'):
            list_of_books = initialized_books_data_source.books_between_years(None, arguments.years[1])
        elif (arguments.years[0].lower() != 'none' and arguments.years[1].lower() == 'none'):
            list_of_books = initialized_books_data_source.books_between_years(arguments.years[0], None)
        elif (arguments.years[0].lower() == 'none' and arguments.years[1].lower() == 'none'):
            list_of_books = initialized_books_data_source.books_between_years(None, None)
        else:
            list_of_books = initialized_books_data_source.books_between_years(arguments.years[0], arguments.years[1])
    
    for book in list_of_books:
        print(book.title+' ('+book.publication_year+')')


if __name__ == '__main__':
    main()
