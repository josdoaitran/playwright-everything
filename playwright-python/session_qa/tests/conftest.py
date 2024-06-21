import pytest
@pytest.fixture(scope="module")
def define_scope_module():
    print("\nThis method will be executed 1 time before all tests - Module 1")
    prepare_test = "All steps in precondition are executed"
    yield prepare_test
    print("\nThis method will be executed 1 time after all tests are executed - Module 2")
