def binary_search_visual(arr, target):
    lo, hi = 0, len(arr) - 1
    step = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"Step {step}: lo={lo}, mid={mid}, hi={hi} | array: {arr}")
        if arr[mid] == target:
            print(f"Found at index {mid}")
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
        step += 1
    print("Not found")
    return -1

if __name__ == "__main__":
    arr = [1,3,5,7,9,11,13,15,17,19]
    target = int(input("Enter target to search: "))
    binary_search_visual(arr, target)
