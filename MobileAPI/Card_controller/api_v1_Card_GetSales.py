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


def test_get_card_sales_for_resident(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "languageId": "hye",
        "residence": 1
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetSales', json=budget_acc,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)

def test_get_card_sales_for_nonresident(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    get_card_sales = {
        "languageId": "hye",
        "residence": 2
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetSales', json=get_card_sales,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)

def test_get_card_sales_empty_language(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    get_card_sales= {
        "languageId": "",
        "residence": 1
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetSales', json=get_card_sales,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_card_sales_wrong_res_type(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    get_card_sales = {
        "languageId": "hye",
        "residence": 50
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/Card/GetSales', json=get_card_sales,
                             headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)