import unittest, tempfile
import main
class TestCore(unittest.TestCase):
    def test_import(self):
        self.assertTrue(hasattr(main,"__name__"))
    def test_graph_has_edges(self):
        self.assertGreater(main.build().number_of_edges(),0)
    def test_citations(self):
        r=main.query('medical imaging')
        self.assertTrue(r['sources'])
        self.assertTrue(all('id' in x for x in r['sources']))
    def test_abstain(self):
        self.assertTrue(main.query('zzzzzz')['abstained'])

if __name__=="__main__":unittest.main()
