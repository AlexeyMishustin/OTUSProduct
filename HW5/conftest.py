import pytest

@pytest.fixture()
def parser(request):
    return request.config.getoption

def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru/",help="set url api")
    parser.addoption("--status",default="200",help="set status response")
