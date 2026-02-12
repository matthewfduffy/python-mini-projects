# Log the time it takes for code to execute

import time

start = time.time()

# Code Block Here

# For Testing
for i in range (10000):
    True

end = time.time()
print("Time Elapsed:", end - start)