class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        
        for letter in sentence:
            alphabet.add(letter)
            
        return len(alphabet) == 26
        