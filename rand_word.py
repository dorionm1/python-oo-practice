"""Python random word generator."""

# def word_counter(filepath):
#     file = open(filepath, "r")
#     count = 0
#     for line in file:
#         if line != "\n":
#             count += 1
#     print(f"{count} words read")
import random
    
class WordFinder:
    def __init__(self, filepath):
        self.filepath = filepath
        self.words = self.get_words()

    def get_words(self):
        file = open(self.filepath, "r")
        word = []
        for line in file:
            if line != "\n":
                word.append(line)
        file.close()
        return word      
    
    def word_counter(self):
        return len(self.words)

    def random(self):
        rand_index = random.randint(0, len(self.words))
        rand_wrd = self.words[rand_index]
        return rand_wrd[:-1]
    
class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.filepath = filepath
    
    def special_random(self):
        """Removes '#' from list so valid list item is always returned."""
        cleanList = [x for x in self.words if not x.startswith('#')]
        rand_index = random.randint(0, len(cleanList)-1)
        rand_wrd = cleanList[rand_index]
        if '\n' in rand_wrd:
            return rand_wrd[:-1]
        else:
            return rand_wrd

    

    