import timeit

def start():
 start = timeit.default_timer()
 return start

def end(start):
 stop = timeit.default_timer()
 execution_time = stop - start
 print("Program Executed in :",execution_time) #It returns time in sec