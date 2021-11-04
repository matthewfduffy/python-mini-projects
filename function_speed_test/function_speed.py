def measure_time(func):
	def wrapper(*args, **kwargs):
		from time import time
		start = time()
		result = func(*args, **kwargs) 
		print(f"Elapsed time is {time() - start} ms")
		return result
	return wrapper


@measure_time
def add(x,y):
    return x + y


print(add(2,5))