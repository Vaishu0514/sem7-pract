import random

def quick_sort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort_deterministic(left) + [pivot] + quick_sort_deterministic(right)

def quick_sort_randomized(arr):
    """Quick sort using a randomized pivot selection."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    return quick_sort_deterministic(arr)

# Generate a random list of integers
arr = [random.randint(1, 100) for _ in range(100)]
"""
n = int(input("Enter array length: "))
arr = []
for i in range (0,n):
    x = int(input("Enter array element: "))
    arr.append(x)
"""
import time
start_time = time.time()
deterministic_result = quick_sort_deterministic(arr.copy())
end_time = time.time()
deterministic_time = end_time - start_time
start_time = time.time()
randomized_result = quick_sort_randomized(arr.copy())
end_time = time.time()
randomized_time = end_time - start_time
print("Deterministic Quick Sort:")
print("Sorted array:", deterministic_result)
print("Time taken:", deterministic_time, "seconds")
print("\nRandomized Quick Sort:")
print("Sorted array:", randomized_result)
print("Time taken:", randomized_time, "seconds")
