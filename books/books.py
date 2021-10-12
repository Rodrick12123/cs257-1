#This is code by Lysander Miller and Thea Traw
#Revised by Thea Traw

import argparse
import booksdatasource
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function')
    parser.add_argument('--titles', '-t', nargs='*',default='NoData', help='sort by titles')
    parser.add_argument('--sort', '-s',nargs='?',default='NoData', help='provides option to sort titles by')
    parser.add_argument('--authors', '-a',nargs='*',default='NoData',  help='sort by authors')
    parser.add_argument('--years', '-y',nargs='*',default='NoData', help='sort by years')
    parser.add_argument('--moreHelp', '-mh','-?',nargs='*',default='NoData', help='provides more information on search')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    initialized_books_data_source = booksdatasource.BooksDataSource("books1.csv")
    arguments = get_parsed_arguments()
    
    if arguments.moreHelp != 'NoData':
        file = open('usage.txt', 'r')
        contents = file.read()
        print(contents)
    elif arguments.authors != 'NoData':
        handle_author_call(initialized_books_data_source, arguments)
    elif arguments.titles != 'NoData':
        handle_title_call(initialized_books_data_source, arguments)
    elif arguments.years != 'NoData':
        handle_years_call(initialized_books_data_source, arguments)
                
def handle_title_call(initialized_books_data_source, arguments):
    
    sorted_by_year = False
    
    if arguments.sort == 'year':
        sorted_by_year = True

    list_of_books = []
    if len(arguments.titles) == 0:
        if not sorted_by_year:
            list_of_books = initialized_books_data_source.books(None)
        else:
            list_of_books = initialized_books_data_source.books(None, 'year')
    else:
        if not sorted_by_year:
            for title in arguments.titles:
                list_of_books += initialized_books_data_source.books(title)
        else:
            for title in arguments.titles:
                list_of_books += initialized_books_data_source.books(title, 'year')
   
    #in case there were multiple search terms
    if not sorted_by_year:
        list_of_books = sorted(list_of_books, key=lambda book: (book.title))
    else:
        list_of_books = sorted(list_of_books, key=lambda book: (book.publication_year, book.title))


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
