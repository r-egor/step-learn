import allure, pytest, requests
from page.API.api_for_project import Url, Headers


@allure.feature("Проект")
@allure.story("Проверка чего")
def test_api_vacancies_of_the_day():
    response = requests.request("GET", Url.url_vacancies_of_the_day, headers=Headers.headers)
    with allure.step('Проверка статус код 200, Вакансии дня'):
        assert response.status_code == 200


def test_api_hh():
    response = requests.request("GET", Url.url_hh, headers=Headers.headers)
    with allure.step('Проверка статус код 200, Подключение к HH'):
        assert response.status_code == 200
