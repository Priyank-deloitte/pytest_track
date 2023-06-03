import pytest


@pytest.fixture(autouse=True, scope="function")
def print_testcase_execution(request):
    test_name = request.node.name
    print(f"Started Testcase {test_name}")

    yield

    print(f"Completed Testcase {test_name}")