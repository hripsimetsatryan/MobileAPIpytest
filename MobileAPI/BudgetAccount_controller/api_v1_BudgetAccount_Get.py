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
        "userName": "Hripsime",
        "password": "Aa-12345"
    }
    response = requests.post(sign_in_url, json=sign_in_data, headers=api_headers)
    assert response.status_code == 200
    access_token = response.json()['data']['token']
    assert access_token is not None
    # print('Access token:', access_token)
    return access_token


def test_get_branches(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "900000000027"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['data']
    assert data is not None
    print(data)

def test_get_branches_string(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "string"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_branches_empty(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": ""
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_branches_max_length(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "1111111111111111111"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_branches_min_length(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "1"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_branches_wrong_acc(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "90000000018"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)

def test_get_branches_symbols(api_headers):
    access_token = test_sign_in(api_headers)
    authorized_headers = api_headers.copy()
    authorized_headers['Authorization'] = f'Bearer {access_token}'
    budget_acc = {
        "budgetAccountNumber": "---------"
    }
    response = requests.post('https://onapipre.conversebank.am/api/v1/BudgetAccount/Get', json=budget_acc, headers=authorized_headers)
    assert response.status_code == 200
    data = response.json()['errors']
    assert data is not None
    print(data)