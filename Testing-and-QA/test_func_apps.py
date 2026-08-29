import func_apps

import os


class TestDuplicate:
    num_file_templ = 'testnum_temp.txt'
    nums_file_testor = 'testnums.txt'

    def setup_class(self):
        shutil.copy(TestDuplicate.num_file_templ,
                    TestDuplicate.nums_file_testor)

    def teardown_class(self):
        os.remove(TestDuplicate.nums_file_testor)

    def test_doublelines(self):
        func_apps.doublelines(TestDuplicate.nums_file_testor)
        num_before = [int(line) for line in open(TestDuplicate.num_file_templ)]
        num_update = [int(line)
                      for line in open(TestDuplicate.nums_file_testor)]
        for num_before, num_update in zip(num_before, num_update):
            assert int(num_update) == int(num_before) * 2

    def test_duplicate(self):
        assert func_apps.duplicate(10) == 20

    def test_duplicate_type():
        with pytest.raises(TypeError):
            apps.duplicate('Hi')
