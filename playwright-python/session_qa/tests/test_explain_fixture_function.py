from session_qa.tests.conftest import define_scope
def test_one(define_scope):
    print("\nDoing 01 test case")
    assert define_scope == "All steps in precondition are executed"

def test_two(define_scope):
    print("\nDoing 02 test case")
    assert define_scope == "All steps in precondition are executed"
