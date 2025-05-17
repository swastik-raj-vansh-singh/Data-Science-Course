# Multithreading 

# simple code 
import time 

def print_number():
    for i in range (5):
        time.sleep(2)
        print(f"number is {i}")

def print_letter():
    for i in "abcd":
        time.sleep(1)
        print(f" letter is {i}")

start = time.time()
print_number()
print_letter()

end  =time.time()- start
print(end)

# this code take 14 sec to run 



# using threads
import threading
import time 

def print_number():
    for i in range (5):
        time.sleep(1)
        print(f"number is {i}")

def print_letter():
    for i in "abcd":
        time.sleep(1)
        print(f" letter is {i}")


# creating 2 threads
t1= threading.Thread(target=print_number)
t2= threading.Thread(target=print_letter)

start= time.time()
# start the threads
t1.start()
t2.start()

# wait for the process to complete 
t1.join()
t2.join()

end = time.time() - start
print(end)

# this code take 5 sec to run which is faster that above 
