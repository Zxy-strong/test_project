import pytest

class Test_ABC:
              # 函数级开始
    def setup_class(self):
        print("start")
              # 函数级结束
    def teardown_class(self):
        print("end")
    def test_a(self):
        assert "1" in "hhh", "失败了"
    def test_b(self):
        assert True

if __name__ == '__main__':
    pytest.main(["-s", "test001.py"])