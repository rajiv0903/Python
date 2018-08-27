'''
Created on Aug 6, 2018
@author: rajiv
'''
import sys
from urllib.request import urlopen

def fetch_words(url): #Function Definition
    """Fetch list of words from URL.
    
    Args: 
        url: The URL of UTF-8 text document
        
    Returns: 
        A list of strings containing the words from 
        the document
    """
    """
    Scopes: 
        Local
        Enclosed
        Global
        Built In
    """
    with urlopen(url) as story:
        story_words= []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
                
    return story_words

def print_words(story_words):    # print_words is Module Scope
    for word in story_words:     # word and story_words in Local Scope
            print(word)

def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_words(words)
    
if __name__ == '__main__': #Main function
    main()
