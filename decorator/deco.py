import time

def go_to_work():

    start_walk = time.time()
    print("Walking...")
    time.sleep(1)
    end_walk = time.time()
    print("Walking took", end_walk - start_walk)
    result = end_walk - start_walk
    print(f'result: {result}')

go_to_work()