import pytest
import requests


@pytest.fixture
def api_headers():
    return {
        'Content-Type': 'application/json',
        'X-API-KEY': 'I12lkdg5jshfjshgfOywItioreito36tVeu',
        'x-deviceid': 'yiusdkdieebdfjhdgk'
    }


def test_sign_in(api_headers):
    sign_in_url = 'https://onapipre.conversebank.am/api/v1/Account/SignIn'
    sign_in_data = {
        "userName": "BenjaminT",
        "password": "Aa-12345"
    }
    response = requests.post(sign_in_url, json=sign_in_data, headers=api_headers)
    assert response.status_code == 200
    access_token = response.json()['data']['token']
    assert access_token is not None
    # print('Access token:', access_token)
    return access_token


def test_card_block(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_block = {
        "cardNumber": "4832910001564364"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/Block', json=card_block,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)


def test_card_empty(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_block = {
        "cardNumber": ""
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/Block', json=card_block,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

    # card -i nisheri sahmanapakum chka, regex chka, tar u symbol tuyl a talis, urishi carder ela tuyl talis grel


def test_card_unblock(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_unblock = {
        "cardNumber": "4832910001564364",
        "expirationDate": "2028-01-25T00:00:00+04:00"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/Block', json=card_unblock,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)


def test_card_unblock_empty(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_unblock = {
        "cardNumber": "",
        "expirationDate": "2028-01-25T00:00:00+04:00"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/Block', json=card_unblock, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    data1 = response.json()['success']
    assert data is not None
    print(data, data1)




