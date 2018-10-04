import pytest
'''
	and if you need to have access to the actual exception info you may use:
'''

def test_recursion_depth():
	with pytest.raises(RuntimeError) as excinfo:
		def hello():
			hello()
		hello()
	assert 'maximum recursion' in str(excinfo.value)