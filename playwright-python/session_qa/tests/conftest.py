import pytest
@pytest.fixture(scope="session")
def define_scope():
    print("\nThis method will be executed - Before Test")
    prepare_test = "All steps in precondition are executed"
    yield prepare_test
    print("\nThis method will be executed - After test")
