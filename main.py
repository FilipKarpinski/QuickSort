 
def partition(arr, low, high):
    j = low
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]

    return j

def quicksort_rec(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_rec(arr, low, pivot_index - 1)
        quicksort_rec(arr, pivot_index + 1, high)

def quicksort(arr):
    quicksort_rec(arr, 0, len(arr) - 1)


ARRAY = [6, 3, 8, 2, 6, 4, 5, 9, 9, 7]

if __name__ == "__main__":
    arr = ARRAY
    print(arr, 'input')
    quicksort(arr)
    print(arr, 'output')
