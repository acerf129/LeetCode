def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L)and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
def printList(arr):
    for n in arr:
        print(n,end=" ")
    print()
if __name__=='__main__':
    arrs=[12, 11, 13, 5, 6, 7]
    print("Given array:",end="\n")
    printList(arrs)
    mergeSort(arrs)
    print("Sorted array:",end="\n")
    print(arrs)