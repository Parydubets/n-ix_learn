import random
import time

random_number = random.randint(1, 10)

start_time = time.time()
time.sleep(random_number)
end_time = time.time()

print(end_time-start_time)