import pytest


@pytest.mark.parametrize('test', [2, 5, 6, 5])
def test_one(test):
    print(test + 42)
    assert 1 == 1


@pytest.fixture(scope='session')
def hello():
    print('тест зпустился')
    yield
    print('тест закончен')



