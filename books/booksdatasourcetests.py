#This is code by Thea Traw and Lysander Miller
from booksdatasource import Book, Author, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')
    def tearDown(self):
        pass
    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
    def test_a_noneCase(self):
        self.smaller_data_source = BooksDataSource('testNone.csv')
        whatShouldBeReturned = [Author('Brontë', 'Charlotte'),Author('Márquez', 'Gabriel'),Author('Wodehouse', 'Pelham')]
        self.assertEqual(self.smaller_data_source.authors(None), whatShouldBeReturned)
    def test_a_alphabeticallyBySurname(self):
        self.smaller_data_source = BooksDataSource('a_alphabeticallyBySurname.csv')
        whatShouldBeReturned = [Author('Dunnewold', 'Mary'),Author('Hosseini', 'Khaled'),Author('Sterne', 'Laurence')]
        self.assertEqual(self.smaller_data_source.authors("a"), whatShouldBeReturned)
    def test_a_alphabeticallyByFirstName(self):
        self.smaller_data_source = BooksDataSource('a_alphabeticallyByFirstName.csv')
        whatShouldBeReturned = [Author('Brontë','Ann'),Author('Brontë','Charlotte'),Author('Brontë','Emily')]
        self.assertEqual(self.smaller_data_source.authors("Brontë"), whatShouldBeReturned)
    def test_a_testTwoAuthors(self):
        whatShouldBeReturned = [Author('Gaiman', 'Neil'),Author('Pratchett','Terry')]
        listOne = self.data_source.authors("Pratchett")
        listTwo = self.data_source.authors("Gaiman")
        listThree = listOne + listTwo
        listThree = sorted(listThree, key=lambda x: (x.surname, x.given_name))
        self.assertEqual(listThree, whatShouldBeReturned)
    def test_a_typoTest(self):
        self.assertEqual(self.data_source.authors('f1re'), [])
        
    def test_t_typoTest(self):
        self.assertEqual(self.data_source.books("f1re"), [])
    def test_t_defaultTest(self):
        whatShouldBeReturned = [Book('Omoo', 1847, [Author('Melville', 'Herman')])]
        self.assertEqual(self.data_source.books("Omoo"), whatShouldBeReturned)
    def test_t_noneTest(self):
        self.smaller_data_source = BooksDataSource('testNone.csv')
        whatShouldBeReturned = [Book('Jane Eyre', 1847, [Author('Brontë', 'Charlotte')]),Book('Leave it to Psmith', 1923, [Author('Wodehouse', 'Pelham Grenville')]),Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')])]
        self.assertEqual(self.smaller_data_source.books(None), whatShouldBeReturned)
    def test_t_portionTest(self):
        whatShouldBeReturned = [Book('Wuthering Heights', 1847, [Author('Brontë', 'Emily')])]
        self.assertEqual(self.data_source.books("Wu"), whatShouldBeReturned)
    def test_t_alphabeticalByTitle(self):
        self.assertEqual(self.data_source.books('time', 'title'), [Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')]), Book('The Fire Next Time', 1963, [Author('Baldwin', 'James')]), Book('Thief of Time', 1996, [Author('Pratchett', 'Terry')])])
    def test_t_sortByYear(self):
        self.assertEqual(self.data_source.books('time', 'year'), [Book('The Fire Next Time', 1963, [Author('Baldwin', 'James')]), Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')]), Book('Thief of Time', 1996, [Author('Pratchett', 'Terry')])])

    def test_y_startYearNone(self):
        self.assertEqual(self.data_source.books_between_years(None, 1815), [Book('Pride and Prejudice', 1813, [Author('Austen', 'Jane')]), Book('Sense and Sensibility', 1813, [Author('Austen', 'Jane')]), Book('Emma', 1815, [Author('Austen', 'Jane')])]
    def test_y_endYearNone(self):
        self.assertEqual(self.data_source.books_between_years(2018, None), [Book('There, There', 2018, [Author('Orange', 'Tommy')]), Book('Fine, Thanks', 2019, [Author('Dunnewold', 'Mary')]), Book('Boys and Sex', 2020, [Author('Orenstein', 'Peggy')]), Book('The Invisible Life of Addie Larue', 2020, [Author('Schwab', 'V.E.')]
    def test_y_doubleNoneTest(self):
        self.smaller_data_source = BooksDataSource('testNone.csv')
        whatShouldBeReturned = [Book('Jane Eyre', 1847, [Author('Brontë', 'Charlotte')]),Book('Leave it to Psmith', 1923, [Author('Wodehouse', 'Pelham Grenville')]),Book('Love in the Time of Cholera', 1985, [Author('García Márquez', 'Gabriel')])]
        self.assertEqual(self.smaller_data_source.books_between_years(None), whatShouldBeReturned)
    def test_y_inclusiveAndTieBreaker(self):
        self.assertEqual(self.data_source.books_between_years(2005, 2010), [Book('1Q84', 2009, [Author('Murakami', 'Haruki')]), Book('All Clear', 2010, [Author('Willis', 'Connie')]), Book('Blackout', 2010, [Author('Willis', 'Connie')])])

if __name__ == '__main__':
    unittest.main()
