from session_10.basic_pytest.example_method import ExampleCode
# generate pytest to cover ExampleCode.average on example_method
def test_example_average_method():
    assert ExampleCode.average(1, 3) == 2
    assert ExampleCode.average(1, 2)== 1.5
    assert ExampleCode.average(1, 1)== 1
    assert ExampleCode.average(1, 0) == 0.5
    assert ExampleCode.average(1, -1) == 0
    assert ExampleCode.average(1, -2) == -0.5
    assert ExampleCode.average(1, -3)== -1
    assert ExampleCode.average(1, -4) == -1.5
    assert ExampleCode.average(1, -5) == -2

    
def test_example_sum_method():
    assert ExampleCode.sum(1, 3) == 4
    assert ExampleCode.sum(1, 2) == 3
    assert ExampleCode.sum(1, 1) == 2
    assert ExampleCode.sum(1, 0) == 1
    assert ExampleCode.sum(1, -1) == 0


