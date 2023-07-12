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
    time.sleep(2)
    rabota_by.fill_search_input()
    time.sleep(2)
    rabota_by.click_fiend_button()
    time.sleep(2)
    rabota_by.set_radio_button_income_level()
    time.sleep(2)
    rabota_by.scroll_down()
    time.sleep(2)
    rabota_by.set_check_box_speciality()
    time.sleep(2)
    rabota_by.scroll_up()
    time.sleep(2)
    rabota_by.open_first_vacancies()
    time.sleep(2)
    rabota_by.check_page()
    time.sleep(2)
