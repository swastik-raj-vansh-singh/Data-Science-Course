# # -- first lets learn function copy

# def welcome():
#     return "welcome"

# copy = welcome
# print(copy())

# del welcome
# print(copy())


# # -- now learning closures -- function inside the function

# def main_welcome():
#     msg = "hello"
#     def sub_welcome():
#         print("sub welcome")
#         print(msg)

#     return sub_welcome()

# main_welcome()


# Decorators -- function that add extra functionality to to other function without modifying the function 

# def main(func):
#     def sub():
#         print ("me")
#         func()
#         print("who")
#     return sub

# @main
# def passing():
#     print("and")

# passing()


# --------------------------------------------------------------------------

# import time
# def timmer(func):
#     def wrapper(*arg):
#         start = time.time()
#         result = func(*arg)
#         end = time.time()
#         print(f"{func.__name__} take {end-start} time")
#         return (result)
#     return wrapper
  
# @timmer  
# def example(n):
#     time.sleep(2)
    
# example(2)


# def main(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         print(f"funxtion name is {func.__name__} and function value is {result}")
#         return result 
#     return wrapper
    
# @main
# def example(name,greatting):
#     return name,greatting
    
# example("swastik","greatting")















