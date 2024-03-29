import requests


def test_get_api_for_dinamic(parser):
    url = parser("--url")
    status = int(parser("--status"))
    result_request = requests.get(url=url)
    assert result_request.status_code == status
