import re
from collections import deque

def get_graph(filename):
    adjacent_list = {}
    with open(filename, "r") as file:
        for edge in file:
            file_content = re.split('[ \n]', edge)
            if len(file_content) == 3: