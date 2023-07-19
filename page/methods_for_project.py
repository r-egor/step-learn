from page.base_page import BasePage
from page.locators import locators_for_project
from page.API import api_for_project
import allure


class RabotaBy(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://rabota.by')

    def fill_search_input(self):
        with allure.step("В поле поиска ввести желаемую профессию"):
            self.find_element(locators_for_project.search_field).send_keys("QA")

    def click_fiend_button(self):
        with allure.step("Нажать на кнопку Найти"):
            self.find_element(locators_for_project.fiend_button).click()

    def set_radio_button_income_level(self):
        with allure.step("Выбрать желаемую зарплату"):
            self.find_element(locators_for_project.radio_button).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 12000);")

    def set_check_box_speciality(self):
        with allure.step("Выбрать желаемую профессию"):
            self.find_element(locators_for_project.check_box).click()

    def scroll_up(self):
        self.driver.execute_script("window.scrollBy(0, -12000);")

    def open_first_vacancies(self):
        with allure.step("Открыть первую вакансию"):
            self.find_element(locators_for_project.first_vacancy).click()

    def check_page(self):
        with allure.step("Проверить что вакансия открыта"):
            self.is_element_present(locators_for_project.respond_button)

    def check_api(self):
        with allure.step("Проверка API"):
            self.make_api_request(api_for_project.vacancies_of_the_day)