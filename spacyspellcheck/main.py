import spacy
import re

nlp = spacy.load('en_core_web_sm')

class SpellCorrector:
    
    def __init__(self, word):
        
        self.word = word
    
    def get_candidates(self, num=5):
        
        """
        Get the best possible words for the mispelled word
        Returns:
            returns the best possible five candidates
        """ 
        
        self.num = num
        
        len_word = len(self.word)
        
        words_list = [x for x in list(set(nlp.vocab.strings)) if len(x) > (len_word - 1) and len(x) < (len_word + 2)]
        
        dist_word = [spacy.matcher.levenshtein(self.word, x) for x in words_list]
        
        sort_index = [i for i, x in sorted(enumerate(dist_word), key=lambda x: x[1])]
        
        candidates_list = [words_list[i].lower() for i in sort_index[0:self.num]]
        
        return candidates_list
      
    
    def get_best(self):
        
        """
        Get the best possible words for the mispelled word
        Returns:
            returns the best probable word
        """        
        
        return self.get_candidates()[0]
