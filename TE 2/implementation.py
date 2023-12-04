import time
import tracemalloc

from dataset_generator import dataset_generator


def branch_bound_partition(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err):
    # If start_index is beyond the end of the array,
    # then all entries have been assigned.
    if start_index >= len(values):
        # We're done. See if this assignment is better than
        # what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            # This is an improvement. Save it.
            best_err[0] = test_err
            best_assignment.clear()
            best_assignment.extend(test_assignment[:])
    else:
        # See if there's any way we can assign
        # the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            branch_bound_partition(values, start_index + 1, total_value, unassigned_value,
                                         test_assignment, test_value + values[start_index], best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            branch_bound_partition(values, start_index + 1, total_value, unassigned_value,
                                         test_assignment, test_value, best_assignment, best_err)


def dp_partition(arr, n):
    Sum = 0
 
    # Calculate sum of all elements
    for i in range(n):
        Sum += arr[i]
    if (Sum % 2 != 0):
        return 0
    part = [0] * ((Sum // 2) + 1)
 
    # Initialize the part array as 0
    for i in range((Sum // 2) + 1):
        part[i] = 0
 
    # Fill the partition table in bottom up manner
    for i in range(n):
 
        # the element to be included
        # in the sum cannot be
        # greater than the sum
        for j in range(Sum // 2, arr[i] - 1, -1):
 
            # check if sum - arr[i]
            # could be formed
            # from a subset
            # using elements
            # before index i
            if (part[j - arr[i]] == 1 or j == arr[i]):
                part[j] = 1
 
    return part[Sum // 2]

def test_partition(set):
    print("Checking for branch and bound partition...")
    start_index = 0
    total_value = sum(set)
    unassigned_value = total_value
    test_assignment = [False] * len(set)
    test_value = 0
    best_assignment = []
    best_err = [float('inf')]
    tracemalloc.start()
    branch_bound_partition(set, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.reset_peak()
    print(f"Current memory usage: {current / 1024:.2f} KB \nPeak memory usage: {peak / (1024):.2f} KB")
    print(best_assignment)

    start_time = time.time()
    branch_bound_partition(set, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)
    end_time = time.time()
    print("Running time: " + str((end_time - start_time) * 1000) + " ms" + "\n" + "-------------------------")
    print(best_assignment)

    print("Checking for dynamic programming partition...")
    tracemalloc.start()
    dp_partition(set, len(set))
    tracemalloc.stop()
    tracemalloc.reset_peak()
    print(f"Current memory usage: {current / 1024:.2f} KB \nPeak memory usage: {peak / (1024):.2f} KB")
    print(best_assignment)

    start_time = time.time()
    dp_partition(set, len(set))
    end_time = time.time()
    print("Running time: " + str((end_time - start_time) * 1000) + " ms" + "\n" + "-------------------------")
    print(best_assignment)

if __name__ == "__main__":
    small_set = dataset_generator(10,100)
    medium_set = dataset_generator(40,400)
    large_set = dataset_generator(80,800)

    small_random_array = list(small_set[2])
    medium_random_array = list(medium_set[2])
    large_random_array = list(large_set[2])

    test_partition(small_random_array)
    test_partition(medium_random_array)
    test_partition(large_random_array)