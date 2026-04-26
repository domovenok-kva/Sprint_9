import allure
from locators.locators import Locators
from page_objects.base_page import BasePage



class CreateAccPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку Создать аккаунт")
    def create_acc_bttn_click(self):
        self.click_element(Locators.create_acc_bttn)

    @allure.step("Заполнить поле Имя")
    def fillin_name_inpt(self, name):
        self.fill_inpt(Locators.name_inpt, name)

    @allure.step("Заполнить поле Фамилия")
    def fillin_surname_inpt(self, surname):
        self.fill_inpt(Locators.surname_inpt, surname)

    @allure.step("Заполнить поле Имя пользователя")
    def fillin_nickname_inpt(self, username):
        self.find_element(Locators.nickname_inpt)
        self.fill_inpt(Locators.nickname_inpt, username)

    @allure.step("Заполнить поле Почта")
    def fillin_email_inpt(self, email):
        self.fill_inpt(Locators.email_inpt, email)

    @allure.step("Заполнить поле Пароль")
    def fillin_passwrd_inpt(self, passwrd):
        self.fill_inpt(Locators.new_password_inpt, passwrd)

    @allure.step("Нажать кнопку Создать аккаунт в форме регестрации")
    def create_bttn_click(self):
        self.click_element(Locators.create_bttn)

    @allure.title("Регистрация пользователя")
    def user_registration(self, user_d):
        self.create_acc_bttn_click()
        self.fillin_name_inpt(user_d['first_name'])
        self.fillin_surname_inpt(user_d['last_name'])
        self.fillin_nickname_inpt(user_d['username'])
        self.fillin_email_inpt(user_d['email'])
        self.fillin_passwrd_inpt(user_d['password'])
        self.create_bttn_click()

    @allure.step("Видимость формы Входа")
    def login_form_is_visible(self):
        return self.find_element(Locators.login_form)

    @allure.step("Отображается корректный адрес страницы")
    def correct_page_adress(self):
        self.driver.implicitly_wait(10)
        return self.page_url()


   