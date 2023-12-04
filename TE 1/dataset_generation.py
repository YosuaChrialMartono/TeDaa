import random

def dataset_generation(filepath, mode, size):
    with open(filepath, 'w') as f:
        random.seed(686)
        if mode == "sorted":
            for i in range(size):
                f.write(str(i) + '\n')
        elif mode == "reverse":
            for i in range(size):
                f.write(str(size - i) + '\n')
        elif mode == "random":
            for i in range(size):
                f.write(str(random.randint(0, 100)) + '\n')
        else:
            print("Invalid Mode")

def main():
    # Debug Dataset generation
    dataset_generation("debug_sorted.txt", "sorted", 10)
    dataset_generation("debug_random.txt", "random", 10)
    dataset_generation("debug_reverse.txt", "reverse", 10)
    
    # Small Dataset generation
    dataset_generation("small_sorted.txt", "sorted", 200)
    dataset_generation("small_random.txt", "random", 200)
    dataset_generation("small_reverse.txt", "reverse", 200)

    # Medium Dataset generation
    dataset_generation("medium_sorted.txt", "sorted", 2000)
    dataset_generation("medium_random.txt", "random", 2000)
    dataset_generation("medium_reverse.txt", "reverse", 2000)

    # Large Dataset generation
    dataset_generation("large_sorted.txt", "sorted", 20000)
    dataset_generation("large_random.txt", "random", 20000)
    dataset_generation("large_reverse.txt", "reverse", 20000)

if __name__ == "__main__":
    main()