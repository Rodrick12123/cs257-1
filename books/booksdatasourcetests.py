#This is code by Thea Traw and Lysander Miller
import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')
    def tearDown(self):
        pass
    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
    def test_a_noneCase(self):
        booksFile = open("books1.csv", "r")
        allBooks = booksFile.readlines()
        booksFile.close()
        cleanTest = []
        for line in allBooks:
            line = line.strip()
            cleanTest.append(line)
        self.assertEqual(self.data_source.authors("None"), allBooks)
    def test_a_alphabeticallyBySurname(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('a_alphabeticallyBySurname.csv')
        whatShouldBeReturned = [Author('Dunnewold', 'Mary'),Author('Hosseini', 'Khaled'),Author('Sterne', 'Laurence')]
        self.assertEqual(self.smaller_data_source.authors("a"), whatShouldBeReturned)
    def test_a_alphabeticallyByFirstName(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('a_alphabeticallyByFirstName.csv')
        whatShouldBeReturned = [Author('Brontë','Ann'),Author('Brontë','Charlotte'),Author('Brontë','Emily')]
        self.assertEqual(self.smaller_data_source.authors("Brontë"), whatShouldBeReturned)
    def test_a_testTwoAuthors(self):
        whatShouldBeReturned = [Author('Gaiman', 'Neil'),Author('Pratchett','Terry')]
        self.assertEqual(self.data_source.authors("Gaiman and Pratchett"), whatShouldBeReturned)

    def test_a_typoTest(self):
        #should be no cases in which a book appears for this search term (so, ok that it passes right now)
        #could also run on books() or even books_between_years()
        self.assertEqual(self.data_source.authors('f1re'), [])
    def test_a_parsingMultipleSearchTerms(self):
        #situation: user enters multiple search terms in a string separated by spaces (i.e. 'Agaths Cristie')
        #should pull up anything that matches any of the terms (i.e. Agatha Cristie)
        self.assertEqual(self.data_source.authors('Agaths Christie'), [Author('Christie', 'Agatha')])

    def test_t_typoTest(self):
        self.assertEqual(self.data_source.books("f1re"), [])
    def test_t_portionOfTitleTest(self):
        whatShouldBeReturned = [Book('The Code of the Woosters'), Book('The Tenant of Wildfell Hall')]
        self.assertEqual(self.data_source.books("Code Hall"), whatShouldBeReturned)
    def test_t_defaultTest(self):
        whatShouldBeReturned = [Book('Omoo')]
        self.assertEqual(self.data_source.books("Omoo"), whatShouldBeReturned)
    def test_t_noneTest(self):
        booksFile = open("books1.csv", "r")
        allBooks = booksFile.readlines()
        booksFile.close()
        cleanTest = []
        for line in allBooks:
            line = line.strip()
            cleanTest.append(line)
        self.assertEqual(self.data_source.books("None"), allBooks)
    def test_t_portionTest(self):
        whatShouldBeReturned = [Book('Wuthering Heights')]
        self.assertEqual(self.data_source.books("Wu"), whatShouldBeReturned)

    def test_t_alphabeticalByTitle(self):
        self.assertEqual(self.data_source.books('time', 'title'), [Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')]), Book('The Fire Next Time', 1963, [Author('Baldwin', 'James')]), Book('Thief of Time', 1996, [Author('Pratchett', 'Terry')])])
    def test_t_sortByYear(self):
        self.assertEqual(self.data_source.books('time', 'year'), [Book('The Fire Next Time', 1963, [Author('Baldwin', 'James')]), Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')]), Book('Thief of Time', 1996, [Author('Pratchett', 'Terry')])])

    def test_y_doubleNoneTest(self):
        booksFile = open("books1.csv", "r")
        allBooks = booksFile.readlines()
        booksFile.close()
        cleanTest = []
        for line in allBooks:
            line = line.strip()
            cleanTest.append(line)
        self.assertEqual(self.data_source.books_between_years("None"), allBooks)
    def test_y_firstTermNone(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('y_firstTermNoneANDLastTermNone.csv')
        whatShouldBeReturned = [Book('Jane Eyre'), Book('Main Street'), Book('Leave it to Psmith')]
        self.assertEqual(self.data_source.books_between_years("None","1923"), whatShouldBeReturned)
    def test_y_lastTermNone(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('y_firstTermNoneANDLastTermNone.csv')
        whatShouldBeReturned = [Book('Leave it to Psmith'),Book('The Fire Next Time'),Book('Love in the Time of Cholera'), Book('Mirror Dance')]
        self.assertEqual(self.data_source.books_between_years("1923", "None"), whatShouldBeReturned)

    def test_y_inclusiveAndTieBreaker(self):
        self.assertEqual(self.data_source.books_between_years(2005, 2010), [Book('1Q84', 2009, [Author('Murakami', 'Haruki')]), Book('All Clear', 2010, [Author('Willis', 'Connie')]), Book('Blackout', 2010, [Author('Willis', 'Connie')])])
    def test_y_typoTest(self):
        #situation: one of the search terms (start year or end year) is not valid (i.e. letters instead of numbers)
        #should raise a TypeError exception if one of the terms is something other than an integer or None
        self.assertRaises(TypeError, self.data_source.books_between_years, 2020, 'hello')

if __name__ == '__main__':
    unittest.main()
