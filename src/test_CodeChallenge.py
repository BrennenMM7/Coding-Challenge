import unittest
import sys
import CodeChallenge
from os import path

class TestApp(unittest.TestCase):
    def setUp(self):
        self.SampleData = path.relpath(".\\sampleData\\testingSample.txt")

    def test_format_data_files(self):
        testList = ['this', 'text', 'is', 'for', 'a', 'sample', 'this', 'text', 'is', 'for', 'a', 'sample']
        WordList = CodeChallenge.format_data_files(self.SampleData)
        self.assertListEqual(WordList, testList)

    def test_analyze_word_list(self):
        testList = ['this', 'text', 'is', 'for', 'a', 'sample', 'this', 'text', 'is', 'for', 'a', 'sample']
        match = [(('this', 'text', 'is'), 2), (('text', 'is', 'for'), 2), (('is', 'for', 'a'), 2),(('for', 'a', 'sample'), 1),(('a', 'sample', 'this'), 1),(('sample', 'this', 'text'), 1)]
        AnalyzedPhrases = CodeChallenge.analyze_word_list(testList)
        self.assertListEqual(AnalyzedPhrases,match)


if __name__ == '__main__':
    unittest.main()
