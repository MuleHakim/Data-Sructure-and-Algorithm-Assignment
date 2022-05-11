#ABINET ANAMO UGR/7110/12
# MULUKEN HAKIM UGR/1110/12

from stack import Stack
def matchGroupings(fileData):
    dict = {"(":")","[":"]","{":"}"}
    listOfKeys = []
    listOfValues = []
    for key in dict.keys():
        listOfKeys.append(key)
    for val in dict.values():
        listOfValues.append(val)
    stack = Stack()
    print("list of each character in the file is : ",fileData)

    for i in fileData:
        # If the characters is different from the symbols that are in listOfKeys an listOfValues, it continues
        if i not in listOfKeys and i not in listOfValues:
            continue
        # If i is in listOfKeys  [  "(","[","{"  ] ,  it pushes to the stack
        elif i in listOfKeys:
            stack.push(i)
        # If i is in listOfValues  [ ")", "}","]"  ] 
        # The length of the stack is greater than zero and
        # If the last element of stack and the keys for i is equal,  it remove the last element of stack
        elif stack.getSize() > 0:
            if i == listOfValues[0] and stack.peek() == listOfKeys[0]:
                stack.pop()
            elif i == listOfValues[1] and  stack.peek() == listOfKeys[1]:
                stack.pop()
            elif i == listOfValues[2] and  stack.peek() == listOfKeys[2]:
                stack.pop()
        # If length of stack is empyty , it returns False
        else:
            return False
    return stack.isEmpty()

def main():
    # it accepts input of the file name
    inputdata = input("Enter a file name: ")
    # it reads the file
    infile = open(inputdata,"r")
    infile2 = list(infile)
    # it accepts the file  character by character and append to the list which is infile3
    infile3 = [i for i in infile2[0]]
    print(matchGroupings(infile3))
    infile.close()

main()