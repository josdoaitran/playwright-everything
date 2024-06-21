import pytest

@pytest.fixture(scope="class")
def define_scope_class():
    print("\nThis method will be executed 1 time before all tests - within a class")
    prepare_test = "All steps in precondition are executed"
    yield prepare_test
    print("\nThis method will be executed 1 time after all tests are executed - within a class")

class TestExample01:
    def test_case_01(self, define_scope_class):
        print("\nDoing 01 test case")
        assert define_scope_class == "All steps in precondition are executed"

    def test_case_02(self, define_scope_class):
        print("\nDoing 02 test case")
        assert define_scope_class == "All steps in precondition are executed"

class TestExampleO2:
    def test_case_03(self):
        print("\nDoing 03 test case")

    def test_case_04(self):
        print("\nDoing 04 test case")
