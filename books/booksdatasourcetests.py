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
        whatShouldBeReturned = ['"Fine, Thanks",2019,Mary Dunnewold (1962-)','The Kite Runner,2003,Khaled Hosseini (1965-)', '"The Life and Opinions of Tristram Shandy, Gentleman",1759,Laurence Sterne (1713-1768)']
        self.assertEqual(self.smaller_data_source.authors("a"), whatShouldBeReturned)
    def test_a_alphabeticallyByFirstName(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('a_alphabeticallyByFirstName.csv')
        whatShouldBeReturned = ['The Tenant of Wildfell Hall,1848,Ann Brontë (1820-1849)','Villette,1853,Charlotte Brontë (1816-1855)','Wuthering Heights,1847,Emily Brontë (1818-1848)']
        self.assertEqual(self.smaller_data_source.authors("Brontë"), whatShouldBeReturned)
    def test_a_testTwoAuthors(self):
        whatShouldBeReturned = ['Good Omens,1990,Neil Gaiman (1960-) and Terry Pratchett (1948-2015)']
        self.assertEqual(self.data_source("Gaiman and Pratchett"), whatShouldBeReturned)
    def test_t_typoTest(self):
        whatShouldBeReturned = ["No results. Please check your entry for typos."]
        self.assertEqual(self.data_source("f1re"), whatShouldBeReturned)
    def test_t_portionOfTitleTest(self):
        whatShouldBeReturned = ['The Code of the Woosters,1938,Pelham Grenville Wodehouse (1881-1975)', 'The Tenant of Wildfell Hall,1848,Ann Brontë (1820-1849)']
        self.assertEqual(self.data_source("Code Hall"), whatShouldBeReturned)
    def test_t_defaultTest(self):
        whatShouldBeReturned = ['Omoo,1847,Herman Melville (1819-1891)']
        self.assertEqual(self.data_source("Omoo"), whatShouldBeReturned)
    def test_t_noneTest(self):
        booksFile = open("books1.csv", "r")
        allBooks = booksFile.readlines()
        booksFile.close()
        cleanTest = []
        for line in allBooks:
            line = line.strip()
            cleanTest.append(line)
        self.assertEqual(self.data_source.authors("None"), allBooks)
    def test_t_portionTest(self):
        whatShouldBeReturned = ['Wuthering Heights,1847,Emily Brontë (1818-1848)']
        self.assertEqual(self.data_source("Wu"), whatShouldBeReturned)
    def test_y_doubleNoneTest(self):
        booksFile = open("books1.csv", "r")
        allBooks = booksFile.readlines()
        booksFile.close()
        cleanTest = []
        for line in allBooks:
            line = line.strip()
            cleanTest.append(line)
        self.assertEqual(self.data_source.authors("None"), allBooks)
    def test_y_firstTermNone(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('y_firstTermNoneANDLastTermNone.csv')
        whatShouldBeReturned = ['Jane Eyre,1847,Charlotte Brontë (1816-1855)', 'Main Street,1920,Sinclair Lewis (1885-1951)', 'Leave it to Psmith,1923,Pelham Grenville Wodehouse (1881-1975)']
        self.assertEqual(self.data_source("None","1923"), whatShouldBeReturned)
    def test_y_lastTermNone(self):
        self.smaller_data_source = booksdatasource.BooksDataSource('y_firstTermNoneANDLastTermNone.csv')
        whatShouldBeReturned = ['Leave it to Psmith,1923,Pelham Grenville Wodehouse (1881-1975)','The Fire Next Time,1963,James Baldwin (1924-1987)','Love in the Time of Cholera,1985,Gabriel García Márquez (1927-2014)', 'Mirror Dance,1994,Lois McMaster Bujold (1949-)']
        self.assertEqual(self.data_source("1923", "None"), whatShouldBeReturned)
if __name__ == '__main__':
    unittest.main()
