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


def test_get_card_oferta_via_post(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "AMD",
        "cardtype": "Woman's Card ",
        "purpose": "Daily living expenses",
        "statedeliverytype": 1
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Data:", data, ", " "Success:", success)


def test_get_card_oferta_via_email(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "AMD",
        "cardtype": "Woman's Card ",
        "purpose": "Daily living expenses",
        "statedeliverytype": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Data:", data, ", " "Success:", success)


def test_get_card_oferta_invalid_id(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 50,
        "currencycode": "AMD",
        "cardtype": "Woman's Card ",
        "purpose": "Daily living expenses",
        "statedeliverytype": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    errors = response.json()['errors']
    success = response.json()['success']
    assert errors is not None
    assert success is not None
    print("Errors:", errors, ", " "Success:", success)


def test_get_card_oferta_empty_currency(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "",
        "cardtype": "Woman's Card",
        "purpose": "Daily living expenses",
        "statedeliverytype": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    errors = response.json()['errors']
    success = response.json()['success']
    assert errors is not None
    assert success is not None
    print("Errors:", errors, ", " "Success:", success)


def test_get_card_oferta_empty_cardType(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "AMD",
        "cardtype": "",
        "purpose": "Daily living expenses",
        "statedeliverytype": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    errors = response.json()['errors']
    success = response.json()['success']
    assert errors is not None
    assert success is not None
    print("Errors:", errors, ", " "Success:", success)


def test_get_card_oferta_empty_purpose(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "AMD",
        "cardtype": "Woman's Card",
        "purpose": "",
        "statedeliverytype": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    errors = response.json()['errors']
    success = response.json()['success']
    assert errors is not None
    assert success is not None
    print("Errors:", errors, ", " "Success:", success)


def test_get_card_oferta_invalid_state_delivery_type(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    card_oferta = {
        "salecardid": 6,
        "currencycode": "AMD",
        "cardtype": "Woman's Card ",
        "purpose": "Daily living expenses",
        "statedeliverytype": 277
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetOferta', json=card_oferta,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Errors:", data, ", " "Success:", success)
