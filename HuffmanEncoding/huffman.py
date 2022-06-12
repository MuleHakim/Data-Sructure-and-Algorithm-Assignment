class HFTNode:
    def __init__(self, freq, character, left=None, right=None):
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
def characters_with_frequency(inputFile):
    # this is a dictionary for characters with their frequencies
    characters = {}
    for i in inputFile:
        if i not in characters.keys():
            characters[i] = 1
        else: 
            characters[i] += 1
    return characters

# This function returns a dictionary which consists a characters with their huffman endoded code (characters_with_codes_Dict)

# This is a dictionary for the characters and with their huffman encoding code value
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
def outputEncoded(inputFile, coding):
    encoding_output = []
    for i in inputFile:
        encoding_output.append(coding[i])
        
    decodedString = ''.join([str(item) for item in encoding_output])    
    return decodedString

# This functions returns the number of bits for the given data before and after compression 
def numOfBits(inputFile, huffman_encoding):
    """
    On modern computer each English characters takes up exactly one byte or eight bits.
    The reason I use 8 bits is that it is big enough to store all the characters, and
    the text does not take up any more space than it absolutely has to and
    also helpful to have a fixed number of bits per character because it makes searching text really fast.
    """
    beforeCompression = len(inputFile) * 8 
    afterCompression = 0
    characters = huffman_encoding.keys()
    for symbol in characters:
        count = inputFile.count(symbol)
        afterCompression += count * len(huffman_encoding[symbol]) 
    return beforeCompression,afterCompression        

def HuffmanTreeEncoding(inputFile):
    charactersDict = characters_with_frequency(inputFile)
    charactersValue = charactersDict.keys()
    # we create this list to store the characters with their frequencies
    listNode = []
    
    # we put all the characters with their frequencies (charactersDict) into a list called nodeList
    # converting characters and frequencies into huffman tree nodes
    for character in charactersValue:
        listNode.append(HFTNode(charactersDict[character],character))
    
    while len(listNode) > 1:
        """
        The greater the frequency, the lower the characters goies in the nodeList

        We remove the first two items in the sorted list of nodesList

        Then we combine into a tree to get new node

        We append the new node to the list and again we sort it.

        This step will be repeated until the loop terminates which means untill the list is empty.

        """

        # sorts the nodeList based on the frequencies
        listNode = sorted(listNode, key=lambda i: i.freq)
        right = listNode[0]
        left = listNode[1]
        left.code = 0
        right.code = 1
        newNode = HFTNode(left.freq+right.freq, left.character+right.character, left, right)
        listNode.remove(left)
        listNode.remove(right)
        listNode.append(newNode)

    # we store a characters with their code (a dictionary which is characters_to_code) with a variable
    huffman_encoding = characters_to_code(listNode[0])
    # we store the returned value from function "numOfBits" in a variable "before" and "after"
    before,after = numOfBits(inputFile, huffman_encoding)
    # we store the returned value from "outputEncoded" in a variable called "encoded_output"
    encoded_output = outputEncoded(inputFile,huffman_encoding)
    
    return encoded_output,before,after,charactersDict,huffman_encoding,listNode[0]

def HuffmanTreeDecoding(encoded_data, nodeList):
    firstNode = nodeList
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            nodeList = nodeList.right   
        elif x == '0':
            nodeList = nodeList.left
        try:
            if nodeList.left.character == None and nodeList.right.character == None:
                pass
        except AttributeError:
            decoded_output.append(nodeList.character)
            nodeList = firstNode
        
    decodedValue = ''.join([str(character) for character in decoded_output])
    return decodedValue        


def test():
    # open the file
    myFile = open("input.txt", "r")
    # read the file
    inputFile = myFile.read()
    encoding, before, after, charactersDict, huffman_encoding, originalList = HuffmanTreeEncoding(inputFile)
    decoding = HuffmanTreeDecoding(encoding,originalList)
       
    print("{0:<25s}{1:<25s}{2:<25s}{3:<25s}".format("Character", "ASCII Code", "Frequency", "Huffman Code"))
    for i in charactersDict.keys():
        print("{0:<25s}{1:<25d}{2:<25d}{3:<25s}".format(str(i), ord(i), charactersDict[i], huffman_encoding[i]))
    
    print("\nTotal bit before compression:", before)
    print("\n_____________________________________________________________________________________________\n")
    print("Encoding output:\n" + encoding)
    print("\n____________________________________________________________________________________________\n_")
    print("Total bit after compression:",  after,"\n")
    # print("Decoding output:", decoding)
    output = open("encoding.txt","w+")
    output.write(encoding)
    output = open("decoding.txt","w+")
    output.write(decoding)

if __name__ == "__main__":
    test()