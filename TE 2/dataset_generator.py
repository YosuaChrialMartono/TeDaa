from random import randint

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
            


    return set_1, set_2, set_1 + set_2


small_dataset = dataset_generator(10,100)
medium_dataset = dataset_generator(40,400)
large_dataset = dataset_generator(80,800)

print(sum(small_dataset[0]), sum(small_dataset[1]))
print(sum(medium_dataset[0]), sum(medium_dataset[1]))
print(sum(large_dataset[0]), sum(large_dataset[1]))
