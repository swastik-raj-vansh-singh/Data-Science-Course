# # iterators --> advance python concept that allow efficient looping and memory management 

# my_list = [1,2,3,4,5]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # StopIteration error


# Generator --> uses yield simple way to build a iterator it store value one by one

def gen():
    yield(1)
    yield(2)
    yield(3)

obj = gen()
print(next(obj))