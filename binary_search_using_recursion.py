def binary_search_using_recursion(arr,element,low,high):
    if low <= high:
        middle = (low + high) // 2
        if arr[middle] == element:
            return f'Element found at index {middle}'
        elif element < arr[middle]:
            return binary_search_using_recursion(arr,element,low,middle-1)
        elif element > arr[middle]:
            return binary_search_using_recursion(arr,element,middle+1,high)

    return 'Element Not Found!'

arr = [-212,-32,1,10,20,100,700,34340,3425400]
print(binary_search_using_recursion(arr,8487541515,0,len(arr)-1))