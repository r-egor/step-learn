import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest, requests, logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import *


# 1. requests - библиотека для отправки HTTP-запросов и получения ответов. Она используется для взаимодействия с веб-серверами и получения данных с веб-страниц.
# 2. selenium - библиотека для автоматизации действий веб-браузера. Она используется для создания автоматизированных тестов, скрапинга данных с веб-страниц и других задач, связанных с веб-браузером.
# 3. pytest - библиотека для создания и выполнения автоматических тестов. Она используется для тестирования кода, написанного на Python, и проверки его корректности.
# 4. logging - библиотека для регистрации сообщений, создания журналов и отслеживания ошибок в приложениях. Она используется для записи сообщений об ошибках и отладочной информации в файлы журналов.
# 5. base64 - библиотека для кодирования и декодирования данных в формате Base64. Она используется для конвертации данных в строковый формат, который может быть передан веб-браузеру.
# 6. DesiredCapabilities - класс, предоставляемый Selenium WebDriver, для настройки параметров браузера. Он используется для установки параметров, таких как версия браузера, операционная система и другие настройки.
# 7. ChromeDriverManager - менеджер драйверов для браузера Google Chrome. Он используется для автоматической загрузки и установки драйвера Chrome, который необходим для работы Selenium WebDriver с браузером Chrome.
# 8. selenium.webdriver.common.proxy - модуль, предоставляемый Selenium WebDriver, для настройки прокси-сервера. Он используется для установки параметров прокси-сервера, таких как адрес и порт.


@pytest.fixture(scope='function')
def driver():

    options = Options()
    service = Service()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
