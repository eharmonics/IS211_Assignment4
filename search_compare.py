import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
   start = time.time()
   pos = 0
   found = False

   while pos < len(a_list) and not found:
       if a_list[pos] == item:
            found = True
       else:
            pos = pos + 1
   elapsed = time.time() - start
   return found , elapsed


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    elapsed = time.time() - start
    return found, elapsed


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    elapsed = time.time() - start
    return found, elapsed


def binary_search_recursive(a_list, item, start = time.time()):

    if len(a_list) == 0:
        elapsed = time.time() - start
        return False, elapsed
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            elapsed = time.time() - start
            return True, elapsed
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, start)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item, start)

if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 10000]
    search_functions = [binary_search_iterative, sequential_search, binary_search_recursive, ordered_sequential_search]
    for search_function in search_functions:
        for size in sizes:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(size)
                # sorting is not needed for sequential search.
                mylist = sorted(mylist)


                check, time_spent = search_function(mylist, -1)
                total_time += time_spent

            avg_time = total_time / 100
            print(f"{search_function.__name__} took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")
