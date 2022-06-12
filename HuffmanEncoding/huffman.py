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

# This function returns a dictionary which consists a characters with their huffman endoded code (characters_with_codes_Dict)

# this is a dictionary for the characters and with their huffman encoding code value
characters_with_codes_Dict = {}
def characters_to_code(huffmanNode, val=''):
    # huffman code for current huffmanNode
    newVal = val + str(huffmanNode.code)

    if(huffmanNode.left):
        characters_to_code(huffmanNode.left, newVal)
    if(huffmanNode.right):
        characters_to_code(huffmanNode.right, newVal)

    if(not huffmanNode.left and not huffmanNode.right):
        characters_with_codes_Dict[huffmanNode.character] = newVal
    return characters_with_codes_Dict        

# This function returns the encoded output for the given data
def outputEncoded(data, coding):
    encoding_output = []
    for i in data:
        encoding_output.append(coding[i])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string