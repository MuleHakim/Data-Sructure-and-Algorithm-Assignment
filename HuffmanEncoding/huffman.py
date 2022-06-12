class HFTNode:
    def init(self, freq, character, left=None, right=None):
        # frequency of the character
        self.freq = freq
        # a character property for the given word
        self.character = character
        # left child nodes
        self.left = left
        # right child nodes
        self.right = right
        # set a direction or code which will be given for the nodes, 0 or 1.
        self.code = ""

# This function returns characters with their frequencies or the dictionary called "charactes" which consists character with their frequencies
def characters_with_frequency(data):
    # this is a dictionary for characters with their frequencies
    characters = {}
    for element in data:
        if element not in characters.keys():
            characters[element] = 1
        else: 
            characters[element] += 1
    return characters