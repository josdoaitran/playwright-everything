import pytest
@pytest.fixture(scope='function')
def define_scope_function():
    print("\nThis method will be executed 1 time before each test")
    yield "resource"
    print("Tearing down will be executed 1 time after each test")

def test_one(define_scope_function):
    print("\nDoing 01 test case")
    assert define_scope_function == "resource"

def test_two(define_scope_function):
    print("\nDoing 02 test case")
    assert define_scope_function == "resource"
