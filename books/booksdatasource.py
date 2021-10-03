#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2021

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

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
        self.listOfAuthors = []
        self.listOfBooks = []
        booksFile = open(books_csv_file_name, "r")
        books = booksFile.readlines()
        booksFileLength = len(books)
        booksFile.close()
        lineNumber = 0
        for line in books:
            editedInformation = []
            twoAuthors = False
            if ('"' in line):
                title = line.split('"')[1]
                everythingButTitle = line.split('"')[2][1:]
                editedInformation.append(title)
                everythingButTitleSeperated = everythingButTitle.split(",")
                for item in everythingButTitleSeperated:
                    editedInformation.append(item)
            else:
                editedInformation = line.split(",")
            if (lineNumber != (booksFileLength -1)):
                    editedInformation[2] = editedInformation[2][:-1]
            authorAndYears = editedInformation[2]
            authorInfo = [authorAndYears]
            if ("and" in authorAndYears):
                splitTwoAuthors = authorAndYears.split("and")
                splitTwoAuthors[0] = splitTwoAuthors[0][:-1]
                splitTwoAuthors[1] = splitTwoAuthors[1][1:]
                authorInfo[0] = splitTwoAuthors[0]
                authorInfo.append(splitTwoAuthors[1])
                twoAuthors = True
            for author in authorInfo:
                authorsFirstName = author.split(" ")[0]
                authorsLastName = ""
                authorsBirthYear = None
                authorsDeathYear = None
                if (len(author.split(" ")) > 3):
                    authorsLastName = author.split(" ")[2]
                else:
                    authorsLastName = author.split(" ")[1]
                if (author[-2:][0] == "-"):
                    authorsBirthYear = author[-6:][:4]
                else:
                    authorsBirthYear = author[-10:][:4]
                    authorsDeathYear = author[-5:][:4]
                myAuthor = Author(authorsLastName, authorsFirstName, authorsBirthYear, authorsDeathYear)
                if ((myAuthor in self.listOfAuthors) == False):
                    self.listOfAuthors.append(myAuthor)
            if (twoAuthors == True):
                listToPass = [self.listOfAuthors[(len(self.listOfAuthors)-1)], self.listOfAuthors[len(self.listOfAuthors)-2]]
                self.listOfBooks.append(Book(editedInformation[0], editedInformation[1], listToPass))
            else:
                listToPass = [self.listOfAuthors[(len(self.listOfAuthors)-1)]]
                self.listOfBooks.append(Book(editedInformation[0], editedInformation[1], listToPass))
            twoAuthors = False
            lineNumber += 1

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        listOfAuthorsWithThisString = []
        if (search_text == 'None' or search_text == None):
            listOfAuthorsSorted = sorted(self.listOfAuthors, key=lambda x: x.surname)
            return listOfAuthorsSorted
        else:
            search_text = search_text.lower()
            for author in self.listOfAuthors:
                if ((search_text in author.surname.lower()) or (search_text in author.given_name.lower())):
                    listOfAuthorsWithThisString.append(author)
            listOfAuthorsWithThisString = sorted(listOfAuthorsWithThisString, key=lambda x: (x.surname, x.given_name))
            return listOfAuthorsWithThisString

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

        selectedBooks = []

        if (search_text=='None' or search_text == None):
            selectedBooks = self.listOfBooks

        #finding books that contain search_term
        else:
            for book in self.listOfBooks:
                if search_text.casefold() in book.title.casefold():
                    selectedBooks.append(book)

        if (sort_by != 'year' or sort_by == 'title'):
            return sorted(selectedBooks, key=lambda book: (book.title))

        else:
            return sorted(selectedBooks, key=lambda book: (book.publication_year, book.title))


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

        startYearNone = False
        endYearNone = False

        if (start_year == 'None' or start_year == None):
            startYearNone = True
        if (end_year == 'None' or end_year == None):
            endYearNone = True

        try:
            
            if (startYearNone == False): 
                x = int(start_year)
            if (endYearNone == False):
                y = int(end_year)
        except ValueError:
            raise ValueError('sorry, invalid input') from None
            quit()

        selectedBooks = []

        #make it so that in Book object, publication years are integers when put in
        #figure out how command line treats ints as arguments so can throw error when string or something

        if (startYearNone == True and endYearNone == True): 
            selectedBooks = self.listOfBooks
            
        elif (startYearNone == True):
            for book in self.listOfBooks:
                if (int(book.publication_year) <= int(end_year)):
                    selectedBooks.append(book)

        elif (endYearNone == True):
            for book in self.listOfBooks:
                if (int(book.publication_year) >= int(start_year)):
                    selectedBooks.append(book)

        else: #neither term is None
            
            for book in self.listOfBooks:
                if (int(book.publication_year) >= int(start_year) and int(book.publication_year) <= int(end_year)):
                    selectedBooks.append(book)
                    
        return sorted(selectedBooks, key=lambda book: (book.publication_year, book.title))

