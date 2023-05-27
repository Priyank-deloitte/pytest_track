import pytest


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass
