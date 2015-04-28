import time

timer = time.time()
final_time = 0
i=5
while (time.time() - timer) < 10:
		i=i+1
		final_time = time.time()
print final_time - timer