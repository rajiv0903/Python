'''
Created on Aug 12, 2018

@author: rajiv
'''
import os
import unittest

def analyze_text(filename):
    
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TextAnalysisTest(unittest.TestCase):
    
    def setUp(self):
        self.filename= 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in great civil way\n'
                    'testing whether that nation,\n'
                    'or\n'
                    'can long endure');
    
    def tearDown(self):
        try:
            os.remove(self.filename);
        except:
            pass
    
    def test_functiona_runs(self):
        analyze_text(self.filename);
    
    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 4);
        
    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 85);
        
    def test_no_deletion(self):
        analyze_text(self.filename);
        self.assertTrue(os.path.exists(self.filename));
        
    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foo');
        

if __name__ == '__main__':
    unittest.main();
    
