""" Ques1O. Exponential Backoff
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting
from 1 second, but stops after 5 retries. """

import time

wait_time = 1
retries = 5
attempt = 0

while attempt < retries:
    print("Attempts Done: ", attempt + 1, "------ Wait Time:", wait_time )
    time.sleep(wait_time)  # Pauses the program for wait_time seconds
    wait_time *= 2   # This technique is called Exponential Backoff
    attempt += 1

# 🔁 Full Execution Timeline
# | Attempt | Printed Wait Time | Actual Sleep Time |
# | ------- | ----------------- | ----------------- |
# | 1       | 1                 | 1 seconds         |
# | 2       | 2                 | 2 seconds         |
# | 3       | 4                 | 4 seconds         |
# | 4       | 8                 | 8 seconds         |
# | 5       | 16                | 16 seconds        |

