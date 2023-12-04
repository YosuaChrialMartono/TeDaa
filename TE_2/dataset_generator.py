from random import randint
import random

def dataset_generator(set_size, max_number=100):
    """
    Generates a dataset of size set_size with numbers ranging from 1 to max_number
    """
    new_set_size = set_size//2
    set_1 = []
    set_2 = []
    for i in range(new_set_size):
        rand_num = randint(1, max_number)
        while rand_num in set_1:
            rand_num = randint(1, max_number)
        set_1.append(rand_num)

    for i in range(new_set_size):
        rand_num = randint(1, max_number)
        while rand_num in set_1 or rand_num in set_2:
            rand_num = randint(1, max_number)
        set_2.append(rand_num)

    sum_diff = sum(set_1) - sum(set_2)
    while True:
        if sum_diff != 0:
            rand_index = randint(0, new_set_size - 1)
            element = set_2[rand_index] + sum_diff
            if element not in set_2:
                if element not in set_1:
                    set_2[rand_index] = element
                    break
    print(sum(set_1), sum(set_2), sum(set_1 + set_2))


    return set_1, set_2, set_1 + set_2

def dataset_generation(filepath, high_sum, size=10):
    with open(filepath, 'w') as f:
        random.seed(686)
        output = dataset_generator(size,high_sum)
        for i in output[2]:
            f.write(str(i) + '\n')

dataset_generation("TE 2/dataset/small_dataset.txt", 100, 10)
dataset_generation("TE 2/dataset/medium_dataset.txt", 200, 40)
dataset_generation("TE 2/dataset/large_dataset.txt", 400, 80)