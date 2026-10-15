import random
import time

def bubble_sort_unoptimized(arr):
    """
    Standard Bubble Sort: Always performs full O(N^2) comparisons,
    even if the list gets sorted early.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_optimized(arr):
    """
    Optimized Bubble Sort: Uses a swapped flag for an early stop
    if no elements were swapped during a pass (O(N) best-case).
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Early termination if no swaps occurred
        if not swapped:
            break
    return arr

def run_profiling_workload():
    # Size set to generate a noticeable execution window
    ARRAY_SIZE = 3000
    NUM_RUNS = 10
    
    print(f"Starting workload: Array Size = {ARRAY_SIZE}, Runs = {NUM_RUNS}...\n")
    
    # Generate identical base arrays for fair comparison
    datasets = [[random.randint(1, 100000) for _ in range(ARRAY_SIZE)] for _ in range(NUM_RUNS)]

    # 1. Profile Unoptimized
    print("Running Unoptimized Bubble Sort...")
    start_time = time.time()
    for dataset in datasets:
        _ = bubble_sort_unoptimized(dataset.copy())
    unoptimized_time = time.time() - start_time
    print(f"Unoptimized Total Time: {unoptimized_time:.2f} seconds\n")

    # 2. Profile Optimized
    print("Running Optimized Bubble Sort...")
    start_time = time.time()
    for dataset in datasets:
        _ = bubble_sort_optimized(dataset.copy())
    optimized_time = time.time() - start_time
    print(f"Optimized Total Time: {optimized_time:.2f} seconds\n")

if __name__ == "__main__":
    run_profiling_workload()