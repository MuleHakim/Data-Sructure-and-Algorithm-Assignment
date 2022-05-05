# By picking median as a pivot

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        firstElement = lst[0]
        middleElement = lst[len(lst)//2]
        lastElement = lst[-1]
        if firstElement <= middleElement <= lastElement:
            pivot = lst.pop(len(lst)//2)
        elif lastElement <= middleElement <= firstElement:
            pivot = lst.pop(len(lst)//2)
        elif middleElement <= firstElement <= lastElement:
            pivot = lst.pop(0)
        elif lastElement <= firstElement <= middleElement:
            pivot = lst.pop(0)
        else:
            pivot = lst.pop()
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