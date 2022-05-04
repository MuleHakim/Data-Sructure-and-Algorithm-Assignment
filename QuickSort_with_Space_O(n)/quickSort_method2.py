# By picking the last element as pivot.

def partition(lst,low,high):
   i = low-1
   pivot = lst[high] 
   for j in range(low,high):
      if lst[j] <= pivot:
         i = i+1
         lst[i],lst[j] = lst[j],lst[i]
   lst[i+1],lst[high] = lst[high],lst[i+1]
   return ( i+1 )

def quickSort(lst,low,high):
   if low < high:
        res = partition(lst,low,high)
        quickSort(lst, low, res-1)
        quickSort(lst, res+1, high)
        return lst

def main():
    lst = [12,32,6,55,8,76,11,0,9,15,23,44,99,65,29,33,41,17,38,]
    print(quickSort(lst,0,len(lst)-1))

main()