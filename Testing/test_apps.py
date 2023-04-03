import apps
import pytest


def test_duplicate():
    assert apps.duplicate(10) == 20

def test_duplicate_type():
	with pytest.raises(TypeError):
		apps.duplicate('Hi')
