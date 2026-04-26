import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from data.urls import Urls

@pytest.fixture
def driver():
    options = ChromeOptions()
    options.set_capability('acceptInsecureCerts', True)
    capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }
    driver = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub", desired_capabilities=capabilities, options=options)
    driver.maximize_window()
    driver.get(Urls.main_url)
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    fake = Faker("en_US")
    userdata = {'first_name': fake.first_name(), 
                'last_name': fake.last_name(), 
                'username': fake.user_name(), 
                'email': fake.email(), 
                'password': fake.password()}
    yield userdata

@pytest.fixture
def data_for_recip_name():
    fake = Faker("ru_RU")
    recip_name = fake.sentence(nb_words=3, variable_nb_words=True)
    yield recip_name

@pytest.fixture
def data_for_ingrid_quantity():
    fake = Faker()
    ingrid_quant = fake.random_int(min = 1, max = 500)
    yield ingrid_quant

@pytest.fixture
def data_for_minutes():
    fake = Faker()
    minutes_gen = fake.random_int(min = 3, max = 120)
    yield minutes_gen

@pytest.fixture
def data_for_desctiption():
    fake = Faker("ru_RU")
    description = fake.text(max_nb_chars = 250)
    yield description

@pytest.fixture
def random_number_for_chckbx():
    fake = Faker()
    random_number = fake.random_int(min = 1, max = 7)
    return random_number

@pytest.fixture
def random_letter_for_ingrid():
    fake = Faker("ru_RU")
    all_russian = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    all_russian.append('ё')
    allowed_letters = [ch for ch in all_russian if ch not in {'ъ', 'ы', 'ь', 'ю'}]
    random_letter = fake.random_element(elements=allowed_letters)
    return random_letter
