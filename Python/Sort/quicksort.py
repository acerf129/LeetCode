def partition(array,low,high):
    pivot=array[high]
    #pointer for greater element
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            #swap element
            array[i],array[j]=array[j],array[i]
    #swap pivot
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        #on left pivot
        quicksort(array, low, pi-1)
        #on right pivot
        quicksort(array, pi+1, high)

arr=[10,7,8,9,1,5]
print("Unsorted Array:",arr)
quicksort(arr,0,len(arr)-1)
print(f'Sorted Array{arr}')