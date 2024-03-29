import requests, json, pytest


def test_check_active_site():
    request = requests.get('https://dog.ceo/dog-api/')
    assert request.status_code == 200


def test_get_all_breeds():
    request = requests.get('https://dog.ceo/api/breeds/list/all')
    assert is_json(request.text) == True


def test_get_all_breeds_status():
    request = requests.get('https://dog.ceo/api/breeds/list/all')
    assert request.status_code == 200


def test_get_random_breeds():
    request = requests.get('https://dog.ceo/api/breeds/image/random')
    assert is_json(request.text) == True


def test_get_random_breeds_status():
    request = requests.get('https://dog.ceo/api/breeds/image/random')
    assert request.status_code == 200


def test_get_all_sub_breeds():
    request = requests.get('https://dog.ceo/api/breed/hound/list')
    assert is_json(request.text) == True


def test_get_all_sub_breeds_status():
    request = requests.get('https://dog.ceo/api/breed/hound/list')
    assert request.status_code == 200


@pytest.mark.parametrize("Pets", ("basenji", "akita"))
def test_get_one_breeds_status_200(Pets):
    request = requests.get(f'https://dog.ceo/api/breed/{Pets}/images/random')
    assert request.status_code == 200


@pytest.mark.parametrize("Pets", ("Biba", "Boba"))
def test_get_one_breeds_status_404(Pets):
    request = requests.get(f'https://dog.ceo/api/breed/{Pets}/images/random')
    assert request.status_code == 404


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True
