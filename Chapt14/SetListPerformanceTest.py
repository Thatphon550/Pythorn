import random
import time

NUMBER_OF_ELEMENTS = 10000

lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

s = set(lst)

startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time()
runTime = (endTime - startTime) * 1000
print(f"To test if {NUMBER_OF_ELEMENTS} elements are in the set, the runtime is {runTime:.2f} milliseconds")

startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
endTime = time.time()
runTime = (endTime - startTime) * 1000
print(f"To test if {NUMBER_OF_ELEMENTS} elements are in the list, The run time is {runTime:.2f} milliseconds")
