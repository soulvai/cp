def merge_sort(arr,n):
    p=2

    while(p<=n):
        i=0
        while(i<n-1):
            l=i
            
            h=i+p
            mid=min((h+l)//2,n)
            # this part main part i may forgot
            h=min(h,n)
            # this part main part i may forgot
            print(l,mid,h,p)
            
            merge(arr,l,mid,h)
            # print(arr)
            i=i+p
            
        p=p*2    
    if(p//2<n):
        merge(arr,0,p//2,n)        



def merge(arr, left_start, mid, right_end):
    n1 = mid - left_start 
    n2 = right_end - mid
    
    left = arr[left_start:mid]
    right = arr[mid:right_end]
    # this technique is awsome
    

    i, j, k = 0, 0, left_start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage:
arr = [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print('real:',arr)
# arr=[1,3,5,2,4,6]
merge_sort(arr,19)
# merge(arr,4,6,8)
print(arr)
