from a import test1,test2
import pytest


class t(object):
    def test3(self,test1, test2):
        u = test1
        p = test2
        assert u == 'leo'
        assert p == '123456'
        print('传入多个fixture参数正确')


# if __name__ == '__main__':
