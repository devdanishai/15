import pytest

@pytest.fixture()
def setup():
    print("i will be execting first")

def test_fixturesDemo():
    print("i will execute steps in fixtureDemo method")

