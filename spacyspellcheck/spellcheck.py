import spacy
import re

nlp = spacy.load('en_core_web_sm')

class SpellCorrector:
    
    def __init__(self, sentence):
        
        self.sentence = sentence 
    
    def get_candidates(self, word, num=5):
        
        """
        Get the best possible words for the misspelt word
        Returns:
            returns the best possible five candidates
        """
        
        self.word = word
        self.num = num
        
        len_word = len(self.word)
        words_list = [x for x in list(set(nlp.vocab.strings)) if len(x) > (len_word - 1) and len(x) < (len_word + 2)]
        dist_word = [spacy.matcher.levenshtein(self.word, x) for x in words_list]
        sort_index = [i for i, x in sorted(enumerate(dist_word), key=lambda x: x[1])]
        candidates_list = [words_list[i].lower() for i in sort_index[0:self.num]]
        
        return candidates_list
    
    def get_possible_misspelled(self):
        
        """
        Gives the most possible words that could be misspelt
        Returns:
            returns the possible words corrected that could be misspelt
        """

        possible_list = []
        list_words = self.sentence.split(' ')
        for word in list_words:
            c_word = self.get_candidates(word, 5)[0]
            if c_word != word:
                possible_list.append(c_word)
                
        return possible_list
    
    def get_best(self, word, num=5):
        
        """
        Get the best possible words for the misspelt word
        Returns:
            returns the best probable word
        """        
        
        self.word = word
        self.num = num
        
        return self.get_candidates(self.word, self.num)[0]
