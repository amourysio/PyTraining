# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
# *********************************

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a = Process(target=counter,args=(2500000000,))
    b = Process(target=counter, args=(2500000000,))
    c = Process(target=counter, args=(2500000000,))
    d = Process(target=counter, args=(2500000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print(f"Finished in:", time.perf_counter(),"seconds")
    # print(f"Finished in:{time.perf_counter()}seconds")


main()
# if __name__ == "main":
#     main()