import pytest
import requests


@pytest.fixture
def api_headers():
    return {
        'Content-Type': 'application/json',
        'X-API-KEY': 'I12lkdg5jshfjshgfOywItioreito36tVeu',
        'x-deviceid': 'yiusdkdieebdfjhdgk'
    }


def query_params_arm():
    return {
        'cardNumber': '4847040000980057'
    }

def query_params_usa():
    return {
        'cardNumber': '487'
    }
def query_params_invalid():
    return {
        'cardNumber': '484'
    }

def test_sign_in(api_headers):
    sign_in_url = 'https://onapipre.conversebank.am/api/v1/Account/SignIn'
    sign_in_data = {
        "userName": "Hripsime",
        "password": "Aa-12345"
    }
    response = requests.post(sign_in_url, json=sign_in_data, headers=api_headers)
    assert response.status_code == 200
    access_token = response.json()['data']['token']
    assert access_token is not None
    # print('Access token:', access_token)
    return access_token


def test_card_country_check_arm(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    params_data_arm = query_params_arm()
    response = requests.get('https://onapipre.conversebank.am/api/v1/Card/CountryCheck', params=params_data_arm,
                            headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Data:", data, ", " "Success:", success)


def test_card_country_check_usa(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    params_data_usa = query_params_usa()
    response = requests.get('https://onapipre.conversebank.am/api/v1/Card/CountryCheck', params=params_data_usa,
                            headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Data:", data, ", " "Success:", success)


def test_card_country_check_invalid(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    params_data_invalid = query_params_invalid()
    response = requests.get('https://onapipre.conversebank.am/api/v1/Card/CountryCheck', params=params_data_invalid,
                            headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    success = response.json()['success']
    assert data is not None
    assert success is not None
    print("Errors:", data, ", " "Success:", success)