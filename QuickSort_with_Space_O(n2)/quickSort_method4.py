#  By picking a random element as a pivot.

import random
def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        randomIndex = random.randint(0,len(lst)-1)
        pivot = lst.pop(randomIndex)
        lowerPart = []
        greaterPart = []
        for i in lst:
            if i > pivot:
                greaterPart.append(i)
            else:
                lowerPart.append(i)
    return quickSort(lowerPart) + [pivot] + quickSort(greaterPart)

def main():
    lst = [12,32,6,55,8,76,11,0,9,15,23,44,99,65,29,33,41,17,38]
    print(quickSort(lst))

main()