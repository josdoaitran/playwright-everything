import pytest

# @pytest.fixture()
# def status_tc():
#     return {
#         "id": 123,
#         "status": "Passed"
#     }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }
