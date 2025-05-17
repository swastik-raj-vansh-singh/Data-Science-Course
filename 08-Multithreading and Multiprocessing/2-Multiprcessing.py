# it allow you to create process that return in parallel

import multiprocessing
import time 

def square():
    for i in range(5):
        time.sleep(1)
        print(f"square of {i} is {i*i}")

def cube():
    for i in range(5):
        time.sleep(1)
        print(f"cube of {i} is {i*i*i}")

if __name__ == "__main__":
    # create 2 process
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t = time.time()

    # Starting the process
    p1.start()
    p2.start()


    # wait for the threads to complete
    p1.join()
    p2.join()

    end= time.time() - t
    print(end)

# time take is 5 sec and they are running as seperate process and both these process have seperate memory 