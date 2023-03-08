"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    
    def __init__(self,path):
        file = open(path) 
        self.b = self.words_read(file)
        print(f"{len(self.b)} words read")        
        
    def words_read(self, file):
        '''
        Returns word from file, while stripping the \n character from each 
        '''
        return [x.strip() for x in file]
                        
    def random(self):
        '''
        uses imported random to grab from read file list, after stripped
        '''
        return random.choice(self.b)