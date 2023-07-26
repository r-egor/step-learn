import time
import allure
import pytest
from page import methods_for_project
from conftest import driver


@allure.feature("Проект")
@allure.story("Проверка чего")
@pytest.mark.usefixtures("driver")
def test_project(driver):
    rabota_by = methods_for_project.RabotaBy(driver)
    rabota_by.open()

    steps_data = [
        ('Enter a vacancy', rabota_by.fill_search_input, 2),
        ('Click find button', rabota_by.click_find_button, 2),
        ('Set radio button', rabota_by.set_radio_button_income_level, 2),
        ('Scroll down', rabota_by.scroll_down, 2),
        ('Set check box', rabota_by.set_check_box_speciality, 2),
        ('Scroll up', rabota_by.scroll_up, 2),
        ('Open first vacancies', rabota_by.open_first_vacancies, 2),
        ('Check open first vacancy', rabota_by.check_page, 2),
    ]

    for step_name, step_func, delay in steps_data:
        try:
            with allure.step(step_name):
                step_func()
        except Exception as e:
            with allure.step(f"Error in Step: {step_name}"):
                allure.attach(str(e), "Error Details")
            raise
        time.sleep(delay)
