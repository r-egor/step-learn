from selenium.webdriver.common.by import By

# Main title
main_title = (By.XPATH, "(//h3[@data-qa='bloko-header-3'])[1]")

# Main search
search_field = (By.XPATH, "//input[@id='a11y-search-input']")

# Button Find
find_button = (By.XPATH, "//span[@class='supernova-search-submit-text']")

# Vacancies search
vacancy_search = (By.XPATH, "//h1[@class='bloko-header-section-3']")

# Income level
radio_button = (By.XPATH, "(//label[@class='bloko-radio'])[2]")

# Check box
check_box = (By.XPATH, "//span[@data-qa][contains(text(), 'Тестировщик')]")

# Requisite
property_in_footer = (By.XPATH, "//*[@id='HH-React-Root']/div/div[3]/div[2]/div/div/div[2]/div/div[2]/p[3]/text()")

# First vacancy after set
first_vacancy = (By.XPATH, "(//span[@data-page-analytics-event='vacancy_search_suitable_item'])[1]")

# The button "respond"
respond_button = (By.XPATH, "(//span[text()='Откликнуться'])[1]")

# The title Vacancy
vacancy_title = (By.XPATH, "(//*[contains(text(), 'QA')])[6]")
