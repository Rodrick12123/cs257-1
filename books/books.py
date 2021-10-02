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
    print(arguments.searchterms)
    #think I should remove this loop
    for term in arguments.searchterms:
        term = term.split(" ")
        arguments = term[0] + " " + term[1]
        searchTerm = []
        i = 2
        while i < len(term):
            searchTerm = searchTerm.append(term[i])
            i+=1
        for term in searchTerm:
            if (arguments == '--titles year' or arguments == '-t year'):
                print(booksdatasource.books(term, 'year'))
            elif (arguments == '--titles title' or arguments == '-t title' or arguments == '--titles' or arguments == '-t'):
                print(booksdatasource.books(term, 'title'))
            elif (arguments == '--authors' or arguments == '-a'):
                print(booksdatasource.authors(term))
            elif (arguments == '--years' or arguments == '-y'):
                print(booksdatasource.books_between_years(term))
            else:
                print("Not a valid command. You can access help through")
if __name__ == '__main__':
    main()
