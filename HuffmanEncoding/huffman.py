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

# This functions returns the number of bits for the given data before and after compression 
def numOfBits(data, huffman_encoding):
    """
    On modern computer each English characters takes up exactly one byte or eight bits.
    The reason I use 8 bits is that it is big enough to store all the characters, and
    the text does not take up any more space than it absolutely has to and
    also helpful to have a fixed number of bits per character because it makes searching text really fast.
    """
    beforeCompression = len(data) * 8 
    afterCompression = 0
    characters = huffman_encoding.keys()
    for symbol in characters:
        count = data.count(symbol)
        afterCompression += count * len(huffman_encoding[symbol]) 
    return beforeCompression,afterCompression        

def HuffmanTreeEncoding(data):
    charactersDict = characters_with_frequency(data)
    charactersValue = charactersDict.keys()
    # we create this list to store the characters with their frequencies
    nodesList = []
    
    # we put all the characters with their frequencies (charactersDict) into a list called nodeList
    # converting characters and frequencies into huffman tree nodes
    for character in charactersValue:
        nodesList.append(HFTNode(charactersDict[character], character))
    
    while len(nodesList) > 1:
        """
        The greater the frequency, the lower the characters goies in the nodeList

        We remove the first two items in the sorted list of nodesList

        Then we combine into a tree to get new node

        We append the new node to the list and again we sort it.

        This step will be repeated until the loop terminates which means untill the list is empty.

        """