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


# MULTITHREADING WITH THREAD POOL EXECUTOR
from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(2)
    return (f" number is {number}")

number = [1,2,3,4,5,6]

with ThreadPoolExecutor(max_workers=6) as executor:
    result = executor.map(print_number,number)

    for i in result:
        print(i)     



# real world example
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://en.wikipedia.org/wiki/Main_Page',
    'https://en.wikipedia.org/wiki/President_of_Uruguay'
]

def fetch(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"fetched {len(soup.text)} chars from {urls}" )
    # print(f"{len(response.content)} chars") 

threads = []
for url in urls:
    t= threading.Thread(target=fetch,args=(url,))

    threads.append(t)
    t.start()

for thread in threads:
    thread.join()


# other way to do the above code is by using thread pool executor

from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

urls = [
    'https://en.wikipedia.org/wiki/Main_Page',
    'https://en.wikipedia.org/wiki/President_of_Uruguay'
]

def fetch(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"fetched {len(soup.text)} chars from {urls}" )
    # print(f"{len(response.content)} chars") 


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(fetch,urls)
        