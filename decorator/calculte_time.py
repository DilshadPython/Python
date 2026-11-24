import time


def time_you_need(base):
    def enhance(*args, **kwargs):
        start_time = time.perf_counter()

        base(*args, **kwargs)

        end_time = time.perf_counter()
        print(f"Time took {end_time - start_time:.2f} seconds")

    return enhance


@time_you_need
def walking_to_works(destination):
    print(f"Walking to {destination}")
    time.sleep(3)

walking_to_works("work")

@time_you_need
def walking_to_university(destination):
    print(f"Walking to {destination}")
    time.sleep(5)

walking_to_university('University')

@time_you_need
def walking_home(destination):
    print(f"Walking to {destination}")
    time.sleep(5)

walking_home('home')

@time_you_need
def compare_time(destination):
    print(f"Comparing {destination}")
    time.sleep(3)

compare_time("destination")
