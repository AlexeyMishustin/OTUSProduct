import requests, pytest


def test_check_active_site():
    request = requests.get('https://www.openbrewerydb.org/')
    assert request.status_code == 200, "Check by 200 status for site"


@pytest.mark.parametrize(("ID,Status"), (
("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", 200), ("b54b16e1-ac3b-4bff-a11f-f7ae9ddc23345353", 404)))
def test_get_signle_blewery_status(ID, Status):
    request = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{ID}')
    assert request.status_code == Status, f"Create ID = {ID}"

@pytest.mark.parametrize("Count",(3,5,7,9,10))
def test_get_blewery_list(Count):
    request = requests.get(f'https://api.openbrewerydb.org/v1/breweries?per_page={Count}')
    assert request.status_code == 200, "check by 200 status for Count blewery"

@pytest.mark.parametrize("TypeBlewery",('micro','regional','contract'))
def test_get_blewery_list_by_type(TypeBlewery):
    request = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_type={TypeBlewery}')
    assert request.status_code == 200, f"check by 200 status by {TypeBlewery}"

@pytest.mark.parametrize(("TypeBlewery","Count"),(('micro',3),('regional',5),('contract',7)))
def test_get_blewery_list_by_type(TypeBlewery,Count):
    request = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_type = {TypeBlewery} & per_page = {Count}')
    assert request.status_code == 200, f"check by 200 status where type = {TypeBlewery} and Count = {Count}"