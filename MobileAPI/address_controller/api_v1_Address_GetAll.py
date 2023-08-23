import pytest
import requests
from MobileAPI.helpers.sign_in import test_sign_in


@pytest.fixture
def api_headers():
    return {
        'Content-Type': 'application/json',
        'X-API-KEY': 'I12lkdg5jshfjshgfOywItioreito36tVeu',
        'x-deviceid': 'yiusdkdieebdfjhdgk'
    }


def test_address_getAll(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    response = requests.get('https://onapipre.conversebank.am/api/v1/Address/GetAll?languageId=hye', headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)
