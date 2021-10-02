#This is code by Lysander Miller and Thea Traw

import argparse
import booksdatasource

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Sorts books and authors')
    parser.add_argument('searchterms', metavar='search', nargs='+', help='search function--put in your search term here')
    parser.add_argument('--titles', '-t', default='--titles', help='sort by titles')
    parser.add_argument('--authors', '-a', default=None,  help='sort by authors')
    parser.add_argument('--years', '-y', default=None, help='sort by years')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    arguments = get_parsed_arguments()
    for term in arguments.searchterms:
        term = term.split(" ")
        arguments = term[0] + " " + term[1]
        searchTerm = ""
        i = 2
        while i < len(term):
            searchTerm += term[i] + " "
            i+=1
        searchTerm = searchTerm.strip()
        if (arguments == '--titles year' or arguments == '-t year'):
            booksdatasource.books(searchTerm, 'year')
        elif (arguments == '--titles title' or arguments == '-t title' or arguments == '--titles' or arguments == '-t'):
            booksdatasource.books(searchTerm, 'title')
        elif (arguments == '--authors' or arguments == '-a'):
            booksdatasource.authors(searchTerm)
        elif (arguments == '--years' or arguments == '-y'):
            booksdatasource.books_between_years(searchTerm)
        else:
            print("Not a valid command. You can access help through
if __name__ == '__main__':
    main()
