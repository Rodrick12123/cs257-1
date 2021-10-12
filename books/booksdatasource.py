#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

#Revised by Thea Traw

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        self.list_of_authors = []
        self.list_of_books = []

        books_file = open(books_csv_file_name, "r")
        lines_in_books_file = books_file.readlines()
        books_file_length = len(lines_in_books_file)
        books_file.close()

        for line in lines_in_books_file:
            
            parsed_information = BooksDataSource.parse_line(line)
            
            title = parsed_information[0]
            publication_year = parsed_information[1]
            author_info = parsed_information[2]

            processed_list_of_authors = BooksDataSource.process_list_of_authors(author_info)

            authors_list = []

            for author in processed_list_of_authors:

                authors_list.append(author)
                if author not in self.list_of_authors:
                    self.list_of_authors.append(author)
            
            book_to_add = Book(title, publication_year, authors_list)
            self.list_of_books.append(book_to_add)

    def parse_line(line):
        parsed_information = []

        #check if there are quotation marks around title
        if line.find('"') == -1:
            parsed_information = line.split(",")
            
        else:
            #just in case there's also '"' in the book title                                                                              
            index_first_quote = line.find('"')
            index_last_quote = line.rfind('"')

            #everything between quotes                                                                                               
            title = line[(index_first_quote + 1):index_last_quote]

            #everything following the comma after the last quote                                                                     
            publication_and_author_info = line[(index_last_quote + 2):].split(",")                                                                                      

            parsed_information.append(title)
            parsed_information.append(publication_and_author_info[0])
            parsed_information.append(publication_and_author_info[1])
            
        return parsed_information

    def process_author(author_info):

        #separate names and birth & death year                                                                                   
        split_index = author_info.rfind(" ")
        names = author_info[:split_index]
        #birth and death year follow the space (" ") after the last name                                                         
        birth_and_death_year = author_info[(split_index + 2):]

        #just count any "middle" names as part of first name                                                                     
        name_split = names.rfind(" ")
        given_name = names[:name_split]
        surname = names[(name_split + 1):]
                
        #for birth year and death year                                                                                           
        birth_and_death_year_split = birth_and_death_year.split("-")
        birth_year = birth_and_death_year_split[0].split("(")[0]

        #assume no death year                                                                                                    
        death_year = None
        if len(birth_and_death_year_split[1]) > 1: #meaning not just a ")"                                                               
            death_year = birth_and_death_year_split[1].split(")")[0]
            
        return Author(surname, given_name, birth_year, death_year)

    def process_list_of_authors(author_info):
        
        authors = []
        if author_info.find(' and ') == -1:
            sole_author = BooksDataSource.process_author(author_info)
            authors.append(sole_author)

        else:
            author_strings = author_info.split(" and ")
            for author_string in author_strings:
                author = BooksDataSource.process_author(author_string)
                authors.append(author)
        
        return authors 


    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''

        selected_authors = []
        if (search_text == None):
            selected_authors = self.list_of_authors
        else:
            for author in self.list_of_authors:
                if ((search_text.lower() in author.surname.lower()) or (search_text.lower() in author.given_name.lower())):
                    selected_authors.append(author)
        return sorted(selected_authors, key=lambda x: (x.surname, x.given_name))

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''

        selected_books = []

        if (search_text == None):
            selected_books = self.list_of_books

        #finding books that contain search_term
        else:
            for book in self.list_of_books:
                if search_text.lower() in book.title.lower():
                    selected_books.append(book)

        if (sort_by != 'year' or sort_by == 'title'):
            return sorted(selected_books, key=lambda book: (book.title))

        else:
            return sorted(selected_books, key=lambda book: (book.publication_year, book.title))


    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''

        start_year_none = False
        end_year_none = False

        if (start_year == 'None' or start_year == None):
            start_year_none = True
        if (end_year == 'None' or end_year == None):
            end_year_none = True

        try:            
            if (start_year_none == False): 
                x = int(start_year)
            if (end_year_none == False):
                y = int(end_year)
        except ValueError:
            raise ValueError('sorry, invalid input') from None
            quit()

        selected_books = []

        if (start_year_none == True and end_year_none == True): 
            selected_books = self.list_of_books
            
        elif (start_year_none == True):
            for book in self.list_of_books:
                if (int(book.publication_year) <= int(end_year)):
                    selected_books.append(book)

        elif (end_year_none == True):
            for book in self.list_of_books:
                if (int(book.publication_year) >= int(start_year)):
                    selected_books.append(book)

        else: #neither term is None
            
            for book in self.list_of_books:
                if (int(book.publication_year) >= int(start_year) and int(book.publication_year) <= int(end_year)):
                    selected_books.append(book)
                    
        return sorted(selected_books, key=lambda book: (book.publication_year, book.title))


    def books_by_author(self, author):
        books_by_author = []
        for book in self.list_of_books:
            if author in book.authors:
                books_by_author.append(book)
        return books_by_author

