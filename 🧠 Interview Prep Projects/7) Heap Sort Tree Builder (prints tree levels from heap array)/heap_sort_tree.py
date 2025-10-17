def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # build max heap
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    # extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def print_tree(arr):
    # print levels
    level = 0
    i = 0
    n = len(arr)
    while i < n:
        nodes = 2**level
        line = arr[i:i+nodes]
        print("Level", level, ":", line)
        i += nodes
        level += 1

if __name__ == "__main__":
    arr = [3, 9, 2, 1, 4, 5, 7, 6]
    print("Original:", arr)
    heap_sort(arr)
    print("Sorted:", arr)
    # rebuild heap to show tree
    import copy
    arr2 = copy.copy(arr)
    # to show heap structure we build a max heap from original list
    arr3 = [3,9,2,1,4,5,7,6]
    for i in range(len(arr3)//2 -1, -1, -1):
        heapify(arr3, len(arr3), i)
    print("\nHeap levels (after heapify):")
    print_tree(arr3)
