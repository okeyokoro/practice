import unittest
import string


class WordCloudData(object):

    def __init__(self, istring):
        self.words_to_counts = {}
        
        p1 = None
        
        for i,c in enumerate(istring+"!"):
            if c in {"'", "-"}:
                continue
            elif c not in string.ascii_letters:
                if p1 != None:
                    
                    word = istring[p1:i]
                    
                    if not self.words_to_counts.get(word):
                        self.words_to_counts[word] = 1
                    else:
                        self.words_to_counts[word] += 1
                        
                    if word[0] == word[0].lower():
                        if word.title() in self.words_to_counts:
                            count = self.words_to_counts.pop(word.title())
                            self.words_to_counts[word] += count
                        if word.capitalize() in self.words_to_counts:
                            count = self.words_to_counts.pop(word.capitalize())
                            self.words_to_counts[word] += count
                    else:
                        if word.lower() in self.words_to_counts:
                            count = self.words_to_counts.pop(word)
                            self.words_to_counts[word.lower()] += count
                
                    p1 = None
            else:
                if p1 == None:
                    p1 = i

    