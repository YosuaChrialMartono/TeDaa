import time
import tracemalloc
from copy import deepcopy
from sorting_implementation import clustered_binary_insertion_sort, randomized_quick_sort

def dataset_reader(filepath):
    '''This function read the dataset from the file and returns \
        an array containing the dataset.
    '''
    array = []
    with open(filepath, 'r') as f:
        for line in f:
            array.append(int(line))
    return array

def memory_experiment(array, sorting_function):
    '''This function runs the sorting function and prints the memory usage.'''
    tracemalloc.start()
    sorting_function(array, left = 0, right = len(array) - 1)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / (1024 * 1024):.2f} MB")
    print(f"Peak memory usage: {peak / (1024 * 1024):.2f} MB")
    tracemalloc.stop()
    tracemalloc.reset_peak()


def profile_running_time(array, sorting_function):
    '''This function runs the sorting function and prints the running time.'''
    start_time = time.time()
    sorting_function(array, left = 0, right = len(array) - 1)
    end_time = time.time()
    print("Running time: " + str((end_time - start_time) * 1000000))

if __name__ == "__main__":
    small_random_array = dataset_reader('dataset/small_random.txt')
    medium_random_array = dataset_reader('dataset/medium_random.txt')
    large_random_array = dataset_reader('dataset/large_random.txt')

    small_sorted_array = dataset_reader('dataset/small_sorted.txt')
    medium_sorted_array = dataset_reader('dataset/medium_sorted.txt')
    large_sorted_array = dataset_reader('dataset/large_sorted.txt')

    small_reversed_array = dataset_reader('dataset/small_reverse.txt')
    medium_reversed_array = dataset_reader('dataset/medium_reverse.txt')
    large_reversed_array = dataset_reader('dataset/large_reverse.txt')

    testing_array = [[small_random_array, clustered_binary_insertion_sort, "small_random_array"], 
                     [small_random_array, randomized_quick_sort, "small_random_array"],
                     [medium_random_array, clustered_binary_insertion_sort, "medium_random_array"],
                     [medium_random_array, randomized_quick_sort, "medium_random_array"],
                     [large_random_array, clustered_binary_insertion_sort, "large_random_array"],
                     [large_random_array, randomized_quick_sort, "large_random_array"],
                     [small_sorted_array, clustered_binary_insertion_sort, "small_sorted_array"],
                     [small_sorted_array, randomized_quick_sort, "small_sorted_array"],
                     [medium_sorted_array, clustered_binary_insertion_sort, "medium_sorted_array"],
                     [medium_sorted_array, randomized_quick_sort, "medium_sorted_array"],
                     [large_sorted_array, clustered_binary_insertion_sort, "large_sorted_array"],
                     [large_sorted_array, randomized_quick_sort, "large_sorted_array"],
                     [small_reversed_array, clustered_binary_insertion_sort, "small_reversed_array"],
                     [small_reversed_array, randomized_quick_sort, "small_reversed_array"],
                     [medium_reversed_array, clustered_binary_insertion_sort, "medium_reversed_array"],
                     [medium_reversed_array, randomized_quick_sort, "medium_reversed_array"],
                     [large_reversed_array, clustered_binary_insertion_sort, "large_reversed_array"],
                     [large_reversed_array, randomized_quick_sort, "large_reversed_array"]]
    for array in testing_array:
        print(array[2] + ": " + str(len(array[0])) + " elements")
        print(array[1].__name__)
        time_array_test = deepcopy(array[0])
        memory_array_test = deepcopy(array[0])
        profile_running_time(time_array_test, array[1])
        memory_experiment(memory_array_test, array[1])
        assert time_array_test == sorted(array[0])
        assert memory_array_test == sorted(array[0])
        print()