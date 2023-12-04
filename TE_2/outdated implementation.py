import time
import tracemalloc

def dataset_reader(filepath):
    '''This function read the dataset from the file and returns \
        an array containing the dataset.
    '''
    array = []
    with open(filepath, 'r') as f:
        for line in f:
            array.append(int(line))
    return array

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
    # Calculate the sum of all elements in the array
    total_sum = sum(arr)

    # Check if the total sum is even, if not, no partition is possible
    if total_sum % 2 != 0:
        return False

    # Initialize the partition table
    partition_table = [[True for _ in range(n + 1)] for _ in range(total_sum // 2 + 1)]

    # Initialize top row as true
    for i in range(n + 1):
        partition_table[0][i] = True

    # Initialize leftmost column, except partition_table[0][0], as false
    for i in range(1, total_sum // 2 + 1):
        partition_table[i][0] = False

    # Fill the partition table in a bottom-up manner
    for i in range(1, total_sum // 2 + 1):
        for j in range(1, n + 1):
            partition_table[i][j] = partition_table[i][j - 1]

            if i >= arr[j - 1]:
                partition_table[i][j] = partition_table[i][j] or partition_table[i - arr[j - 1]][j - 1]
    return partition_table[total_sum // 2][n]




def test_dp_partition(set):
    print("Checking for dynamic programming partition...")

    tracemalloc.start()
    dp_partition(set, len(set))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.reset_peak()

    print(f"Current memory usage: {current / 1024:.2f} KB \nPeak memory usage: {peak / (1024):.2f} KB")
    print(dp_partition(set, len(set)))

    start_time = time.time()
    dp_partition(set, len(set))
    end_time = time.time()

    print("Running time: " + str((end_time - start_time) * 1000) + " ms" + "\n" + "-------------------------")
    print(dp_partition(set, len(set)))

if __name__ == "__main__":
    small_set = dataset_reader('TE 2/dataset/small_dataset.txt')
    medium_set = dataset_reader('TE 2/dataset/medium_dataset.txt')
    large_set = dataset_reader('TE 2/dataset/large_dataset.txt')

    test_dp_partition(small_set)
    test_dp_partition(medium_set)
    test_dp_partition(large_set)