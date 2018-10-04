# we will test a single test multiple time 
# and test single test multiple times using parametrize
import multiple_test
import pytest

@pytest.mark.parametrize('test_input, expected_output',
							[
								(5, 25),
								(3, 9),
								(8, 64)
							]
						)
def test_collect_sqr(test_input, expected_output):
	result = multiple_test.collect_sqr(test_input)
	assert result == expected_output

