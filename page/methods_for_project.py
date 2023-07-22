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

        # Find title Работа найдётся для каждого
        main_title_found = self.is_elements_text_equal_to(locators_for_project.main_title,
                                                          element_text='Работа найдётся для каждого')
        assert main_title_found, 'Работа найдётся для каждого, элемент не найден'

    def fill_search_input(self):
        with allure.step("В поле поиска ввести желаемую профессию"):
            self.find_element(locators_for_project.search_field).send_keys("QA")

        # Find Button Find
        find_button_found = self.is_element_present(locators_for_project.find_button)
        assert find_button_found, 'Кнопка Найти не найдена'

    def click_find_button(self):
        with allure.step("Нажать на кнопку Найти"):
            self.find_element(locators_for_project.find_button).click()

        # Find name Vacancies "QA"
        vacancies_found = self.is_elements_text_equal_to(locators_for_project.vacancy_search,
                                                         element_text="QA")
        assert vacancies_found, "Вакансии не найдены"

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

        vacancy_title_found = self.is_elements_text_equal_to(locators_for_project.vacancy_title, element_text="QA")
        assert vacancy_title_found, "Заголовок вакансии не найден"
