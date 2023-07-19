import time
import allure
import pytest
from Page import methods_for_project
from Page import base_page
from conftest import driver


@allure.feature("Проект")
@allure.story("Проверка чего")
@pytest.mark.usefixtures("driver")
def test_project(driver):
    rabota_by = methods_for_project.RabotaBy(driver)
    rabota_by.open()

    steps_data = [
        (rabota_by.fill_search_input, 2),
        (rabota_by.click_fiend_button, 2),
        (rabota_by.set_radio_button_income_level, 2),
        (rabota_by.scroll_down, 2),
        (rabota_by.set_check_box_speciality, 2),
        (rabota_by.scroll_up, 2),
        (rabota_by.open_first_vacancies, 2),
        (rabota_by.check_page, 2),
    ]

    for step, delay in steps_data:
        step()
        time.sleep(delay)