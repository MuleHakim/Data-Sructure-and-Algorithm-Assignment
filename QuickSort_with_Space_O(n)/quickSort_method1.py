# By picking the first element as pivot.

def partition(lst, start, end):
    pivot = lst[start]
    low = start + 1
    high = end

    while True:
        while low <= high and lst[high] >= pivot:
            high = high - 1

        while low <= high and lst[low] <= pivot:
            low = low + 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
        else:
            break

    lst[start], lst[high] = lst[high], lst[start]

    return high

def quickSort(lst, start, end):
    if start >= end:
        return

    res = partition(lst, start, end)
    quickSort(lst, start, res-1)
    quickSort(lst, res+1, end)
    return lst

def main():
    lst = [12,32,6,55,8,76,11,0,9,15,23,44,99,65,29,33,41,17,38]
    print(quickSort(lst, 0, len(lst) - 1))

main()
