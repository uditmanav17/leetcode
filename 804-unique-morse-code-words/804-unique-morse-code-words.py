import string as s

class Solution:
    def __init__(self):
        self.mapping = dict(zip(s.ascii_lowercase, [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniques = set()
        for word in words:
            s = ""
            for char in word:
                s+=self.mapping.get(char)
            uniques.add(s)
        return len(uniques)
        