import pytest


@pytest.fixture(scope="function")
def test1():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture()
def test2():
    b = '123456'
    print('传出b')
    return b


