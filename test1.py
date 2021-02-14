import pytest
class Test_1():
    def setup(self):
        print("start")
    def teardown(self):
        print("end")
    def test001(self):
        assert True
    def test002(self):
        assert False
if __name__ == '__main__':
    pytest.main()