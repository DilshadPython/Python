from hiker import global_answer, Hiker

def test_global_function():
    assert global_answer() == 42

def test_instance_method():
    assert Hiker().instance_answer() == 42

def green_traffic_light_pattern():
    return 'All tests passed'


if __name__ == '__main__':
    test_global_function()
    test_instance_method()
    print(green_traffic_light_pattern())
