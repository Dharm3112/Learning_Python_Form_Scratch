import time

wait_time = 1
max_wait_time = 5
attempts = 0


while attempts < max_wait_time:
    print("Wait time: ", attempts + 1 , "Wait Time: ", wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts += 1