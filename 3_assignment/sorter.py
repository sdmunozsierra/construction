"""Sorts collections."""
import time
import timeit
import random


def sort_collection(filename):
    with open(filename, 'r') as fh:
        numbers = [int(x.strip()) for x in fh]
        numbers.sort()
        return numbers


def create_file_random_data(filename, iterations):
    with open(filename, 'w') as fh:
        for x in range(iterations):
            rnd = random.randint(1, iterations*10)
            fh.write(str(rnd) + "\n")


# create_file_random_data("10_elements_random.txt", 10)
# timeit.timeit(sort_collection('10_elements_random.txt'))

if __name__ == '__main__':
    # Random data
    print("Testing sort algorithm with random data")
    time_start = time.time()
    sort_collection('10_elements_random.txt')
    total_time = time.time() - time_start
    print("10 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('100_elements_random.txt')
    total_time = time.time() - time_start
    print("100 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('1000_elements_random.txt')
    total_time = time.time() - time_start
    print("1000 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('10000_elements_random.txt')
    total_time = time.time() - time_start
    print("10000 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('100000_elements_random.txt')
    total_time = time.time() - time_start
    print("100000 elements random time: ", total_time)

    # Sorted data
    print("\nTesting sort algorithm with 1 element unsorted")
    time_start = time.time()
    sort_collection('10_elements_sorted.txt')
    total_time = time.time() - time_start
    print("10 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('100_elements_sorted.txt')
    total_time = time.time() - time_start
    print("100 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('1000_elements_sorted.txt')
    total_time = time.time() - time_start
    print("1000 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('10000_elements_sorted.txt')
    total_time = time.time() - time_start
    print("10000 elements random time: ", total_time)

    time_start = time.time()
    sort_collection('100000_elements_sorted.txt')
    total_time = time.time() - time_start
    print("100000 elements random time: ", total_time)

    print("Complexity is n log n")
