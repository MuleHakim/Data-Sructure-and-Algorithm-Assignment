# By picking median as pivot

def quickSort(lst,first,last):
    if last>first:
        pivotIndex = partition(lst,first,last)
        quickSort(lst,first,pivotIndex-1)
        quickSort(lst,pivotIndex+1,last)
        return lst
def partition(lst,first,last):
    middle = lst[(len(lst)-1)//2]
    pivot = median(first,middle,last)
    low = first + 1
    high = last

    while high>low:
        while low<=high and lst[low]<=pivot:
            low += 1
        while low<=high and lst[high]>pivot:
            high -= 1
        if high>low:
            lst[high],lst[low]=lst[low],lst[high]
    while high>first and lst[high]>=pivot:
        high -= 1
    if pivot > lst[high]:
        lst[first]=lst[high]
        lst[high]=pivot
        return high
    else:
        return first
def median(first,middle,last):
    return max(min(first,middle),min(max(first,middle),last))
def main():
    lst = [12,32,6,55,8,76,11,0,9,15,23,44,99,65,29,33,41,17,38]
    print(quickSort(lst,0,len(lst)-1))

main()