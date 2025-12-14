import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(request):
    # Считываем параметр language из командной строки
    language = request.config.getoption("--language")

    # Настройка браузера
    options = Options()
    options.add_argument('--headless')  # Режим без графического интерфейса
    options.add_argument(f'--lang={language}')  # Устанавливаем язык браузера

    # Создаем экземпляр браузера
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
  
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Set language for the browser")
