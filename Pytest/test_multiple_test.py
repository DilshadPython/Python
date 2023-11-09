# we will test a single test multiple time
# and test multiple test in one test
import multiple_test


def test_collect_sqr():
    result = multiple_test.collect_sqr(5)
    assert result == 25


def test_collect_sqr_1():
    result = multiple_test.collect_sqr(7)
    assert result == 49


def test_collect_sqr_2():
    result = multiple_test.collect_sqr(6)
    assert result == 36
