from page.base_page import BasePage
from page.locators import locators_for_project
import allure


class RabotaBy(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://rabota.by')

        # Find title Работа найдётся для каждого
        main_title = locators_for_project.main_title
        element_text = 'Работа найдётся для каждого'
        main_title_found = self.is_elements_text_equal_to(main_title, element_text=element_text)
        if not main_title_found:
            raise AssertionError('Работа найдётся для каждого, элемент не найден')

    def fill_search_input(self):
        with allure.step("В поле поиска ввести желаемую профессию"):
            self.find_element(locators_for_project.search_field).send_keys("QA")

        # Find Button Find
        find_button = locators_for_project.find_button
        find_button_found = self.is_element_present(find_button)
        if not find_button_found:
            raise AssertionError('Кнопка Найти не найдена')

    def fill_search_input(self):
        with allure.step("В поле поиска ввести желаемую профессию"):
            search_field = self.find_element(locators_for_project.search_field)
            search_field.send_keys("QA")

    def click_find_button(self):
        with allure.step("Нажать на кнопку Найти"):
            self.find_element(locators_for_project.find_button).click()

        # Find name Vacancies "QA"
        vacancies_name = locators_for_project.vacancy_search
        element_text = 'QA'
        vacancies_name_found = self.is_elements_text_equal_to(vacancies_name, element_text=element_text)
        if not vacancies_name_found:
            raise AssertionError("Вакансии не найдены")


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

        vacancy_title = locators_for_project.vacancy_title
        element_text = "QA"
        vacancy_title_found = self.is_elements_text_equal_to(vacancy_title, element_text=element_text)
        if not vacancy_title_found:
            raise AssertionError('Название вакансии не найдено')
