
import pytest
'''
The two line below to make the pytest run with python3 only
'''
# import sys
# py3 = sys.version_info[0] >= 3


@pytest.mark.windows
def test_windows():
    assert True


@pytest.mark.linux
def test_linux():
    assert True


@pytest.mark.mac
def test_mac():
    assert True

# to test pytest -m mac -v or pytest -m linux -v
# if you want to run all the tests except windows
# pytest -m ''not windows' -v
