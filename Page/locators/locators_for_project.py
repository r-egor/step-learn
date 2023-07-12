from selenium.webdriver.common.by import By

# Main search
search_field = (By.XPATH, "//input[@id='a11y-search-input']")

# Button Fiend
fiend_button = (By.XPATH, "//span[@class='supernova-search-submit-text']")

# Vacancies search
vacancy_search = (By.XPATH, "//h1[@class='bloko-header-section-3']")

# Income level
radio_button = (By.XPATH, "(//label[@class='bloko-radio'])[2]")

# Check box
check_box = (By.XPATH, "//span[@data-qa][contains(text(), 'Тестировщик')]")

# First vacancy after set
first_vacancy = (By.XPATH, "(//span[@data-page-analytics-event='vacancy_search_suitable_item'])[1]")

# The button "respond"
respond_button = (By.XPATH, "(//span[text()='Откликнуться'])[1]")
