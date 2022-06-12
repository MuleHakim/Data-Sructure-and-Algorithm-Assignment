# Data-Sructure-and-Algorithm-Assignment 

## Assignment 3 - Huffman Encoding

## Huffman Encoding
### Steps or Algorithm that we use to build huffman tree
|                  Steps    
|-------------------------------------------------------------------
|       Create a leaf node for every character in the input. Build a
Minimum Heap of all leaf nodes.
|       For the Minimum Heap, get the top or the first two nodes
with minimum frequency.
|       Create a new node with frequency equal to the sum of
        frequency of the first two nodes. Make the first as the left
child of the new node and the second as the right child of
the new node. Remove the two nodes and Add the new node
to the Minimum Heap
|      Repeat the above steps until the Minimum Heap has only
one node
|      we used 8 bits which is big enough to store all the
characters
|      The programs takes a file as an input and returns the
output in different files.
|      The program displays characters, ASCII code of characters, frequencies of characters and the huffman code of the characters in one table
|      The program display number of bits before and after compression
|      The program display the encoded output for the given text 
## License

AAiT © [Muluken Hakim](https://github.com/mulehakim)
AAiT © [Abinet Anamo](https://github.com/abi26anamo)
AAiT © Hayat Ibrahim