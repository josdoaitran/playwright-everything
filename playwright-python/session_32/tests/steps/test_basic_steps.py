import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios('../features/test_basic.feature')

@pytest.fixture
def context():
    return {}

@given(parsers.parse('I have the numbers {a:d} and {b:d}'))
def have_numbers(a, b, context):
    context['a'] = a
    context['b'] = b

@when('I add the numbers')
def add_numbers(context):
    context['result'] = context['a'] + context['b']

@then(parsers.parse('the result should be {result:d}'))
def check_result(result, context):
    assert context['result'] == result