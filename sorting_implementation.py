import random
import copy
def clustered_binary_insertion_sort(array):
    '''The function sorts the array in place using \
        clustered binary insertion sort and returns nothing.
    \nIt accepts the following parameters:
    - array: the array to be sorted
    '''
    pop = 0
    for i in range(1, len(array)):
        cop = i
        key = array[cop]
        if key >= array[pop]:
            place = binary_loc_finder(array, pop+1, cop-1, key)
        else:
            place = binary_loc_finder(array, 0, pop-1, key)
        pop = place
        array = place_inserter(array, place, i)
        i += 1

def place_inserter(array, start, end):
    '''The function inserts the element at the end of the subarray to the start of the subarray.
    \nIt accepts the following parameters:
    - array: the array to be modified
    - start: the leftmost index of the subarray
    - end: the rightmost index of the subarray
    '''
    temp = array[end]
    for i in range (end, start, -1):
        array[i] = array[i-1]
    array[start] = temp
    return array


def binary_loc_finder(array, start, end, key):
    '''The function returns the index of the key in the array.
    \nIt accepts the following parameters:
    - array: the array to be searched
    - start: the leftmost index of the array
    - end: the rightmost index of the array
    - key: the key to be searched
    '''
    if start == end:
        if array[start] > key:
            return start
        else:
            return start + 1
    elif start > end:
        return start
    else:
        mid = (end + start) // 2
        if array[mid] < key:
            return binary_loc_finder(array, mid + 1, end, key)
        elif array[mid] > key:
            return binary_loc_finder(array, start, mid - 1, key)
        else:
            return mid
            

def randomized_quick_sort(array, left, right):
    '''The function recursively sorts the array in place and returns nothing.
    \nIt accepts the following parameters:
    - array: the array to be sorted
    - left: the leftmost index of the array
    - right: the rightmost index of the array
    '''
    if left < right:
        pivot = randomized_partition(array, left, right)
        randomized_quick_sort(array, left, pivot - 1)
        randomized_quick_sort(array, pivot + 1, right)
        
def randomized_partition(array, left, right):
    '''The function partitions the array into two parts \
        and returns the index of the pivot.
    \nIt accepts the following parameters:
    - array: the array to be sorted
    - left: the leftmost index of the array
    - right: the rightmost index of the array
    '''
    random_number = random.randint(left, right)
    array[random_number], array[right] = array[right], array[random_number]
    pivot = array[right]
    last_filled = left - 1
    for i in range(left, right):
        if array[i] <= pivot:
            last_filled += 1
            array[last_filled], array[i] = array[i], array[last_filled]
    last_filled += 1
    array[last_filled], array[right] = array[right], array[last_filled]
    return last_filled

def dataset_reader(filepath):
    '''This function read the dataset from the file and returns \
        an array containing the dataset.
    '''
    array = []
    with open(filepath, 'r') as f:
        for line in f:
            array.append(int(line))
    return array

def main():
    array = dataset_reader("debug_random.txt")
    cbis_test_array = copy.deepcopy(array)
    rqs_test_array = copy.deepcopy(array)
    print(array)
    clustered_binary_insertion_sort(array)

    print(array)

if __name__ == "__main__":
    main()
    