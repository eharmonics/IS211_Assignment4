import argparse
# other imports go here

import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
        elapsed = time.time() - start
        return  elapsed


def shellSort(alist):
    start = time.time()
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)


        sublistcount = sublistcount // 2
        elapsed = time.time() - start
        return  elapsed


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    """
    Use Python built-in sorted function
    :param a_list:
    :return: the sorted list
    """
    start = time.time()
    a_list = sorted(a_list)
    return time.time()-start


if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 10000]
    sort_functions = [insertion_sort, shellSort, python_sort]
    for sort_function in sort_functions:
        for size in sizes:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(size)
                # sorting is not needed for sequential search.
                time_spent = sort_function(mylist)
                total_time += time_spent

            avg_time = total_time / 100
            print(f"{sort_function.__name__} took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")
