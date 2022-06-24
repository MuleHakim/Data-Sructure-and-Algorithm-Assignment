import re
from collections import deque

def get_graph(filename):
    adjacent_list = {}
    with open(filename, "r") as file:
        for edge in file:
            file_content = re.split('[ \n]', edge)
            if len(file_content) == 3:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2]]
            elif len(file_content) == 4:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2]]
            elif len(file_content) == 5:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2], file_content[3]]
            elif len(file_content) == 6:
                adjacent_list[file_content[0]] = [file_content[1], file_content[2], file_content[3],
                                                  file_content[4]]