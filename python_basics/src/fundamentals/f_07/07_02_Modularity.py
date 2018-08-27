'''
Created on Aug 6, 2018
@author: rajiv
'''
'''
Modularity using Function
'''

from urllib.request import urlopen

def fetch_words(): #Function Definition
    with urlopen("http://sixty-north.com/c/t.txt") as story:
        story_words= []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    
    for word in story_words:
        print(word)


#fetch_words();
if __name__ == '__main__': #Main function
    fetch_words()